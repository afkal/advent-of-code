import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import gleeunit/should
import simplifile

fn sum_list(list: List(String)) -> Int {
  case list {
    [] -> 0
    [x, ..xs] -> {
      case int.parse(x) {
        Ok(value) -> value + sum_list(xs)
        Error(_) -> sum_list(xs)
        // Skip invalid integers
      }
    }
  }
}

// Calculate the sum of distances of the list items between two lists
fn list_of_distances(list1: List(String), list2: List(String)) -> Int {
  case list1, list2 {
    [], [] -> 0
    [x1, ..xs1], [x2, ..xs2] -> {
      case int.parse(x1), int.parse(x2) {
        Ok(value1), Ok(value2) ->
          int.absolute_value(value2 - value1) + list_of_distances(xs1, xs2)
        _, _ -> list_of_distances(xs1, xs2)
      }
    }
    _, _ -> 0
  }
}

// Part 1. Calculate the sum of distances of the list items between two lists
fn part1(list1: List(String), list2: List(String)) -> Int {
  list_of_distances(
    list1 |> list.sort(string.compare),
    list2 |> list.sort(string.compare),
  )
}

// Calculate the similarity score between two lists
fn similarity_score(list1: List(String), list2: List(String), acc: Int) -> Int {
  case list1 {
    [] -> 0
    [x] -> {
      // Find the count of matching items in list2
      let count = list2 |> list.count(fn(y) { x == y })
      let score = count * { x |> int.parse |> result.unwrap(0) }
      acc + score
    }
    [x, ..xs] -> {
      // Find the count of matching items in list2
      let count = list2 |> list.count(fn(y) { x == y })
      let score = count * { x |> int.parse |> result.unwrap(0) }
      similarity_score(xs, list2, acc + score)
    }
  }
}

// Part 2. Calculate the similarity score between two lists
fn part2(list1: List(String), list2: List(String)) -> Int {
  similarity_score(
    list1 |> list.sort(string.compare),
    list2 |> list.sort(string.compare),
    0,
  )
}

fn formulate_input_data(data: String) -> #(List(String), List(String)) {
  let data_list = data |> string.split("\n")
  // Split the data into two lists
  let list1 =
    data_list
    |> list.map(fn(row: String) {
      row |> string.split("   ") |> list.first() |> result.unwrap("")
    })
  let list2 =
    data_list
    |> list.map(fn(row: String) {
      row |> string.split("   ") |> list.last() |> result.unwrap("")
    })
  #(list1, list2)
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

  // Split the data into two lists
  formulate_input_data(test_data)
  let #(list1, list2) = formulate_input_data(test_data)

  // Part 1
  io.debug(part1(list1, list2))
  // Part 2
  io.debug(part2(list1, list2))
}

// Test functions
// Note that running tests in the src directory requires hacking the gleaunit.gleam file
// to look for tests in the src directory instead of the test directory
// find_files(matching: "**/*.{erl,gleam}", in: "test")
// should be changed to
// find_files(matching: "**/*.{erl,gleam}", in: "src")
// in the do_main() function

pub fn sum_list_test() {
  let list = ["1", "2", "3"]
  let result = sum_list(list)
  result |> should.equal(6)
}

pub fn part1_1_test() {
  let list1 = ["1", "2", "3"]
  let list2 = ["1", "2", "4"]
  let result = part1(list1, list2)
  result |> should.equal(1)
}

pub fn part1_2_test() {
  let list1 = ["1", "4", "4"]
  let list2 = ["2", "3", "5"]
  let result = part1(list1, list2)
  result |> should.equal(3)
}

pub fn part2_1_test() {
  let list1 = ["1", "2", "3"]
  let list2 = ["1", "1", "2"]
  let result = part2(list1, list2)
  result |> should.equal(4)
}

pub fn part2_2_test() {
  let list1 = ["3", "4", "2", "1", "3", "3"]
  let list2 = ["4", "3", "5", "3", "9", "3"]
  let result = part2(list1, list2)
  result |> should.equal(31)
}
