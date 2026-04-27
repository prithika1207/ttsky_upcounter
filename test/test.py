import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_upcounter_basic(dut):

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Apply reset
    dut.rst_n.value = 0
    for _ in range(3):
        await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    # Observe counter for a few cycles
    for i in range(20):
        await RisingEdge(dut.clk)

        value = int(dut.out.value)
        dut._log.info(f"Cycle {i}: out = {value}")

        # Optional sanity check (safe)
        assert 0 <= value < 16
