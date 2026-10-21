import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_count_up(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.en.value = 1
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == 0

    dut.rst.value = 0
    for expected in range(1, 6):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(dut.count.value) == expected


@cocotb.test()
async def test_hold_when_disabled(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.en.value = 1
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst.value = 0

    for _ in range(3):
        await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    held = int(dut.count.value)

    dut.en.value = 0
    for _ in range(4):
        await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.count.value) == held