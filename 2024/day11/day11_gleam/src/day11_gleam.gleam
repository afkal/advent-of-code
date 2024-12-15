import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import gleeunit/should

fn transform_stone(stone: Int) -> Int {
  case stone {
    0 -> 1
    1 -> 2
    2 -> 0
    _ -> stone
  }
}

fn part1(stones: List(Int), round: Int, max_round: Int) -> Int {
  case stones {
    [] -> round
    [stone] -> round
    [stone1, stone2, ..rest] -> {
      let new_round = round + 1
    }
    _ -> round
  }
}

pub fn main() {
  let input = "125 17"
  // Test input
  //let input = "8069 87014 98 809367 525 0 9494914 5"

  let input_list = string.split(input, " ")
  let input_list =
    list.map(input_list, fn(a) { a |> int.parse |> result.unwrap(0) })
  let result = part1(input_list, 0, 25)
  io.print(int.to_string(result))
}

// Tests

pub fn transform_stone_test() {
  let input = 0
  let result = transform_stone(input)
  result |> should.equal(1)
}
