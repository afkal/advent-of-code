import gleam/io
import gleam/string
import gleeunit/should
import simplifile

// Part 1. Find the floor that the instructions take Santa to
fn find_floor(instructions: List(String), floor: Int) -> Int {
  case instructions {
    [] -> floor
    [a] -> {
      case a {
        "(" -> floor + 1
        ")" -> floor - 1
        _ -> floor
      }
    }
    [a, ..tail] -> {
      case a {
        "(" -> find_floor(tail, floor + 1)
        ")" -> find_floor(tail, floor - 1)
        _ -> find_floor(tail, floor)
      }
    }
  }
}

// Part 2. Find the position of the first instruction that takes Santa to the basement
fn find_basement(instructions: List(String), floor: Int, position: Int) -> Int {
  case instructions {
    [] -> position
    [a, ..tail] -> {
      case a {
        "(" -> find_basement(tail, floor + 1, position + 1)
        ")" -> {
          case floor - 1 {
            -1 -> position
            // Found the basement -> return the position
            _ -> find_basement(tail, floor - 1, position + 1)
          }
        }
        _ -> find_basement(tail, floor, position + 1)
      }
    }
  }
}

fn read_file(filename: String) -> String {
  //let file_exists = simplifile.is_file(filename)
  case simplifile.read(filename) {
    Ok(data) -> data
    Error(_) -> "Failed to read config file"
  }
}

// Main function
pub fn main() {
  let filepath = "../input.txt"
  let test_data = read_file(filepath)
  //io.println(test_data)
  // Import the test data
  let instructions = test_data |> string.to_graphemes()
  //io.debug(instructions)
  let floor = find_floor(instructions, 0)
  io.debug(floor)
  let basement = find_basement(instructions, 0, 1)
  io.debug(basement)
}

// Test the functions
pub fn floor_basement1_test() {
  let instructions = ")" |> string.to_graphemes()
  find_floor(instructions, 0)
  |> should.equal(-1)
  find_basement(instructions, 0, 1)
  |> should.equal(1)
}

pub fn floor_basement2_test() {
  let instructions = "))" |> string.to_graphemes()
  find_floor(instructions, 0)
  |> should.equal(-2)
  find_basement(instructions, 0, 1)
  |> should.equal(1)
}

pub fn floor_basement3_test() {
  let instructions = "())" |> string.to_graphemes()
  find_floor(instructions, 0)
  |> should.equal(-1)
  find_basement(instructions, 0, 1)
  |> should.equal(3)
}

pub fn floor_basement4_test() {
  let instructions = ")()" |> string.to_graphemes()
  find_floor(instructions, 0)
  |> should.equal(-1)
  find_basement(instructions, 0, 1)
  |> should.equal(1)
}
