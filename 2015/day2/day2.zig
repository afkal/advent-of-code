// To run:
// zig run day2.zig

const std = @import("std");
const input = @embedFile("input.txt"); // Embed input file at compile time

const print = std.debug.print;

pub fn main() void {
    var total_area: u64 = 0;
    var total_ribbon: u64 = 0;

    var lines = std.mem.tokenize(u8, input, "\n"); // Split input to lines
    var dim: [3]u64 = undefined;
    while (lines.next()) |line| {
        var index: u8 = 0;
        var dimensions = std.mem.tokenize(u8, line, "x");
        while (dimensions.next()) |dimension| {
            dim[index] = std.fmt.parseInt(u64, dimension, 10) catch unreachable;
            index += 1;
        }
        // Sort box edges
        std.mem.sort(u64, &dim, {}, comptime std.sort.asc(u64));

        total_area += (2 * dim[0] * dim[1] + 2 * dim[1] * dim[2] + 2 * dim[2] * dim[0] + dim[0] * dim[1]);
        total_ribbon += 2 * dim[0] + 2 * dim[1] + dim[0] * dim[1] * dim[2];
    }
    print("Part 1, total area: {d}", .{total_area}); // Part1: 1606483
    print("Part 2, total ribbon: {d}", .{total_ribbon}); //Part2: 3842356
}
