SIM = icarus
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(CURDIR)/counter.sv
COMPILE_ARGS += -g2012
COCOTB_TOPLEVEL = counter
COCOTB_TEST_MODULES = test_counter
include $(shell cocotb-config --makefiles)/Makefile.sim