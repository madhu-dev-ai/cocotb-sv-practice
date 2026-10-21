\# cocotb SystemVerilog Practice



Two small designs written in SystemVerilog and verified with cocotb (Python) and Icarus Verilog.



\## 1. Counter (counter.sv)

A 4-bit counter with an enable input.

\- Counts up on every clock edge when `en` is 1

\- Holds its value when `en` is 0

\- Resets to 0 when `rst` is 1

\- Uses `always\_ff`



Tests (test\_counter.py):

\- `test\_count\_up`: after reset, checks the counter goes 1, 2, 3, 4, 5

\- `test\_hold\_when\_disabled`: counts, turns `en` off, checks the value does not change



\## 2. ALU (alu.sv)

A 4-bit ALU with add, subtract, AND and OR. Uses `always\_comb`.



Tests (test\_alu.py):

\- `test\_add`: includes 4-bit wrap-around (15 + 1 = 0)

\- `test\_subtract`: includes wrap-around (0 - 1 = 15)

\- `test\_and\_or`



\## How to run

Requires Icarus Verilog, cocotb and make.



Counter:



&#x20;   make



ALU:



&#x20;   make -f Makefile.alu



\## Tools

SystemVerilog, Python, cocotb, Icarus Verilog

