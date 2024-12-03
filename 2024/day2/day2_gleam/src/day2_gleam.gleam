import aoc_library_gleam
import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string

fn check_levels_desc_damp(levels: List(Int), damp_used: Bool) -> Bool {
  case levels {
    [] -> False
    [level] -> True
    [level, next] ->
      case { level - next } >= 1 && { level - next } <= 3 {
        True -> True
        False -> False
      }
    [level, next, nextnext, ..rest] -> {
      case { level - next } >= 1 && { level - next } <= 3 {
        True -> {
          check_levels_desc_damp([next, nextnext, ..rest], damp_used)
        }
        False -> {
          // Check if we can skip a problematic level
          case
            { level - nextnext } >= 1
            && { level - nextnext } <= 3
            && damp_used == False
          {
            True -> {
              check_levels_desc_damp([nextnext, ..rest], True)
            }
            False -> False
          }
        }
      }
    }
  }
}

fn check_levels_asc_damp(levels: List(Int), damp_used: Bool) -> Bool {
  io.debug(levels)
  case levels {
    [] -> False
    [level] -> True
    [level, next] ->
      case { next - level } >= 1 && { next - level } <= 3 {
        True -> True
        False -> False
      }
    [level, next, nextnext, ..rest] -> {
      case { next - level } >= 1 && { next - level } <= 3 {
        True -> {
          check_levels_asc_damp([next, nextnext, ..rest], damp_used)
        }
        False -> {
          // Check if we can skip a problematic level
          case
            { nextnext - level } >= 1
            && { nextnext - level } <= 3
            && damp_used == False
          {
            True -> {
              check_levels_asc_damp([nextnext, ..rest], True)
            }
            False -> {
              io.println("Check failed: ")
              io.debug(level)
              io.debug(next)
              io.debug(nextnext)
              False
            }
          }
        }
      }
    }
  }
}

fn check_levels_desc(levels: List(Int)) -> Bool {
  case levels {
    [] -> False
    [level] -> True
    // Last level can always be removed
    [level, next, ..rest] -> {
      //io.debug(level - next)
      case { level - next } >= 1 && { level - next } <= 3 {
        True -> {
          //io.debug("Level ok")
          check_levels_desc([next, ..rest])
        }
        False -> False
      }
    }
  }
}

fn check_levels_asc(levels: List(Int)) -> Bool {
  case levels {
    [] -> False
    [level] -> True
    [level, next, ..rest] -> {
      case { next - level } >= 1 && { next - level } <= 3 {
        True -> {
          check_levels_asc([next, ..rest])
        }
        False -> False
      }
    }
  }
}

fn list_of_results_to_int(levels: List(Result(Int, Nil))) -> List(Int) {
  case levels {
    [] -> []
    [level] -> [level |> result.unwrap(0)]
    [level, ..rest] -> {
      case level {
        Ok(value) -> [value] |> list.append(list_of_results_to_int(rest))
        _ -> list_of_results_to_int(rest)
      }
    }
  }
}

fn line_is_safe(line: String) -> Bool {
  let levels =
    line
    |> string.split(" ")
    |> list.map(int.parse)
    |> list_of_results_to_int

  check_levels_desc(levels) || check_levels_asc(levels)
  //io.debug(levels)

  //True
}

fn line_is_safe_part2(line: String) -> Bool {
  let levels =
    line
    |> string.split(" ")
    |> list.map(int.parse)
    |> list_of_results_to_int

  let seed = levels |> list.first() |> result.unwrap(0)
  check_levels_desc_damp(levels, False) || check_levels_asc_damp(levels, False)
  //io.debug(levels)

  //True
}

// Part 1.
fn part1(data: String) -> Int {
  // Split the data into list of lines
  let lines = string.split(data, "\n")
  //io.debug(lines)
  // Filter "safe" lines
  lines |> list.filter(line_is_safe) |> list.length()
}

// Part 2.
fn part2(data: String) -> Int {
  // Split the data into list of lines
  let lines = string.split(data, "\n")
  //io.debug(lines)
  // Filter "safe" lines
  lines |> list.filter(line_is_safe_part2) |> list.length()
}

pub fn main() {
  let input_file = "../input.txt"
  let input = aoc_library_gleam.read_file(input_file)

  io.debug(part1(input))
  //io.debug(part2("1 2 11 4 5"))
}

// Tests
const test_data = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"

// Test Part 1
pub fn part1_test() {
  // Descending normal case
  let assert 2 = part1(test_data)
}

// Test Part 1
pub fn part2_1_test() {
  // Descending normal case
  let assert 4 = part2(test_data)
}

pub fn part2_2_test() {
  // Descending normal case
  let assert 1 = part2("7 6 4 2 1")
  // Ascending normal case
  let assert 1 = part2("1 2 5 8 9")
  // Ascending and descending skip one case
  let assert 1 = part2("1 2 11 4 5")
  let assert 1 = part2("5 4 11 2 1")

  // Descending and ascending try to skip two case
  let assert 0 = part2("1 11 2 12 5")
  let assert 0 = part2("5 12 2 11 1")
}
