import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_upcounter(dut):
    """Test 4-bit up counter"""

    # Start clock (10 ns period)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Apply reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    # Release reset
    dut.rst_n.value = 1

    # Check counting for first 20 cycles
    expected = 0

    for i in range(20):
        await RisingEdge(dut.clk)

        expected = (expected + 1) % 16  # 4-bit wraparound
        assert dut.out.value == expected, \
            f"Mismatch at cycle {i}: expected {expected}, got {dut.out.value}"
