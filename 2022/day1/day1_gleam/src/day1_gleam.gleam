import aoc_library_gleam
import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string

const day1_test = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"

fn calculate_sums_of_chunks(chunks: List(String)) -> List(Int) {
  case chunks {
    [] -> []
    [chunk] -> {
      let lines = string.split(chunk, "\n")
      let sum = aoc_library_gleam.sum_of_int_strings(lines)
      [sum]
    }
    [chunk, ..rest] -> {
      let lines = string.split(chunk, "\n")
      let sum = aoc_library_gleam.sum_of_int_strings(lines)
      [sum] |> list.append(calculate_sums_of_chunks(rest))
    }
  }
}

fn create_sums_of_chunks(data: String) -> List(Int) {
  let chunks = string.split(data, "\n\n")
  calculate_sums_of_chunks(chunks)
}

// Part 1: Calculate the sum of the integers
// in the chunks of input data
fn part1(data: String) -> Int {
  // Create a list of sums of the chunks and return the largest sum
  create_sums_of_chunks(data)
  |> list.sort(int.compare)
  |> list.last()
  |> result.unwrap(0)
}

// Part 2: Get the sum of top 3 sums of the chunks
fn part2(data: String) -> Int {
  // Create a list of sums of the chunks and return the top 3 sums
  create_sums_of_chunks(data)
  |> list.sort(int.compare)
  |> list.reverse
  |> list.take(3)
  |> list.reduce(fn(acc, x) { acc + x })
  |> result.unwrap(0)
}

// Main function
pub fn main() {
  let filepath = "../input.txt"
  let test_data = aoc_library_gleam.read_file(filepath)

  // Test part1 function
  let assert 24_000 = part1(day1_test)

  // Test part2 function
  let assert 45_000 = part2(day1_test)

  io.debug(part1(test_data))
  io.debug(part2(test_data))
}
