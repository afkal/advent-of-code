// To run:
// zig run day1.zig

const std = @import("std");
const input = @embedFile("input.txt"); // Embed input file at compile time


pub fn part1() void {

    var floor: i32 = 0;
    for (input) |char| {
        if (char == '(') {
            floor += 1;
        }
        if (char == ')') {
            floor -= 1;
        }
    }
    std.debug.print("Part 1 answer is: {d} \n", .{floor}); // 138
}

pub fn part2() void {

    var floor: i32 = 0;
    var position: u32 = 0;
    for (input) |char| {
        position += 1;
        if (char == '(') {
            floor += 1;
        }
        if (char == ')') {
            floor -= 1;
        }
        // Check if basement (floor == -1)
        if (floor == -1) {
            std.debug.print("Part 2 answer is: {d} \n", .{position}); // 1771
            break;
        }
    }
    
}

pub fn main() void {
    part1();
    part2();
}