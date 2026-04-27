import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_upcounter(dut):

    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    expected = 0

    for i in range(20):
        await RisingEdge(dut.clk)

        expected = (expected + 1) % 16
        assert dut.out.value == expected, \
            f"FAIL at {i}: expected {expected}, got {dut.out.value}"
