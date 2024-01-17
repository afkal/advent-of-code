// To run:
// zig run day2.zig

const std = @import("std");
const input = @embedFile("input.txt"); // Embed input file at compile time

const print = std.debug.print;

pub fn main() void {

    var total_area: u16 = 0;
    var lines = std.mem.tokenizeAny(u8, input, "\n"); // Split input to lines
    while (lines.next()) |line| {
        print("{s}\n", .{line});

        //const dimensions = std.mem.tokenizeAny(u8, line, "x");
        total_area += 1;
    }
    print("total area: {d}",.{total_area});
}