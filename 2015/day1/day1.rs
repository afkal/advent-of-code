// To run:
// rustc day1.rs | ./day1

use std::fs;

const INPUT_FILE : &str = "input.txt";

fn read_input() -> String {
    return fs::read_to_string(INPUT_FILE)
        .expect("Should have been able to read the file");
}

fn day1() {
    let input = read_input();
    
    let mut floor: i32 = 0;
    let mut position: i32 = 0;
    let mut basemend_found = false;
    for char in input.chars() {
        position += 1;
        if char == '(' {
            floor += 1;
        }
        if char == ')' {
            floor -= 1;
        }
        // Print position if basement
        if floor == -1 && !basemend_found {
            println!("Part 2 answer: {position}"); // 1771
            basemend_found = true;
        }
    }
    println!("Part 1 answer: {floor}"); // 138
    
}

fn main() {
    day1();
}