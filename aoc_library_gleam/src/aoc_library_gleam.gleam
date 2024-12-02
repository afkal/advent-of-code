//// This is the main file for the aoc_library_gleam library.
//// This file is imported in the AoC Gleam projects file.
//// This file contains the functions that will be used in the Advent of Code projects.

// Import the Gleam standard library
import gleam/int
import gleam/io
import gleam/list
import simplifile

// Read the input file for the AoC project 
pub fn read_file(filename: String) -> String {
  //let file_exists = simplifile.is_file(filename)
  case simplifile.read(filename) {
    Ok(data) -> data
    Error(_) -> "Failed to read input file"
  }
}

// Sum a list of integers
pub fn sum_of_int_strings(list: List(String)) -> Int {
  case list {
    [] -> 0
    [x, ..xs] -> {
      case int.parse(x) {
        Ok(value) -> value + sum_of_int_strings(xs)
        Error(_) -> sum_of_int_strings(xs)
        // Skip invalid integers
      }
    }
  }
}

pub fn main() {
  io.println("Hello from aoc_library_gleam!")
}
