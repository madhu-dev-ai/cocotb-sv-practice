import cocotb
from cocotb.triggers import Timer


async def check(dut, a, b, op, expected):
    dut.a.value = a
    dut.b.value = b
    dut.op.value = op
    await Timer(1, unit="ns")
    assert int(dut.result.value) == expected, (
        f"a={a} b={b} op={op}: got {int(dut.result.value)}, expected {expected}"
    )


@cocotb.test()
async def test_add(dut):
    await check(dut, 3, 4, 0, 7)
    await check(dut, 15, 1, 0, 0)


@cocotb.test()
async def test_subtract(dut):
    await check(dut, 9, 4, 1, 5)
    await check(dut, 0, 1, 1, 15)


@cocotb.test()
async def test_and_or(dut):
    await check(dut, 12, 10, 2, 8)
    await check(dut, 12, 10, 3, 14)