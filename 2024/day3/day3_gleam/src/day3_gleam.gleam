import aoc_library_gleam
import gleam/int
import gleam/io
import gleam/list
import gleam/option.{Some}
import gleam/regex.{type Match}
import gleam/result

//fn loop_match(input: List(Match)) {
//  case input {
//    [first, ..rest] -> {
//      let assert Match(x) = first
//    }
//    _ -> io.debug(input |> list.first |> result.unwrap(Match()))
//  }
//}

fn multiply(first: String, second: String) -> Int {
  let first_int = first |> int.parse |> result.unwrap(0)
  let second_int = second |> int.parse |> result.unwrap(0)
  first_int * second_int
}

fn parse_match(match: Match) {
  case match.submatches {
    [Some(first), Some(second)] -> {
      multiply(first, second)
    }
    _ -> panic
  }
  //io.debug(match)
}

pub fn main() {
  //let input =
  "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
  //let input =
  "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  let input = aoc_library_gleam.read_file("../input.txt")

  //Filter out anything between don't() and do()
  //let assert Ok(re) = regex.from_string("don't\\(\\)(.*?)do\\(\\)")
  //let input = regex.replace(re, input, "***THIS BIT IS REMOVED***")
  //io.debug(input)

  // Find matches for multiplication
  let assert Ok(re) = regex.from_string("mul\\((\\d{1,3}),(\\d{1,3})\\)")
  let result = regex.scan(re, input)
  // Loop the result
  let result = result |> list.map(parse_match)
  let result = result |> list.reduce(fn(a, b) { a + b })
  //io.debug(loop_match(result))
  io.debug(result)
}
