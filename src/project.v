module tt_um_upcounter (
    input  wire clk,
    input  wire rst_n,
    output reg  [3:0] out
);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
        out <= 4'b0000;
    else
        out <= out + 4'b0001;
end

endmodule
