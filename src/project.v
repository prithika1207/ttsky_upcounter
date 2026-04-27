module tt_um_upcounter (
    input  wire clk,
    input  wire rst_n,
    input  wire ena,
    output reg  [3:0] out
);

wire enable = ena;  // you can also ignore or force it

always @(posedge clk) begin
    if (!rst_n)
        out <= 4'b0000;
    else if (enable)
        out <= out + 1'b1;
end

endmodule
