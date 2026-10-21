module alu (
    input  logic [3:0] a,
    input  logic [3:0] b,
    input  logic [1:0] op,
    output logic [3:0] result
);

    always_comb begin
        case (op)
            2'd0:    result = a + b;
            2'd1:    result = a - b;
            2'd2:    result = a & b;
            2'd3:    result = a | b;
            default: result = 4'd0;
        endcase
    end

endmodule