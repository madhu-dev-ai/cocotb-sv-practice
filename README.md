\# cocotb SystemVerilog Counter



A 4-bit counter with an enable input, written in SystemVerilog and verified with cocotb (Python) and Icarus Verilog.



\## What it does

\- Counts up on every clock edge when `en` is 1

\- Holds its value when `en` is 0

\- Resets to 0 when `rst` is 1



\## Tests

\- `test\_count\_up`: after reset, checks the counter goes 1, 2, 3, 4, 5

\- `test\_hold\_when\_disabled`: counts, turns `en` off, checks the value does not change



\## How to run

Requires Icarus Verilog, cocotb and make.



&#x20;   make



\## Tools

SystemVerilog, Python, cocotb, Icarus Verilog

