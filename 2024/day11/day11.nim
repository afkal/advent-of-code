import strutils, options

let test_data = "125 17"
let input = "8069 87014 98 809367 525 0 9494914 5"

type Node = object
    value: int
    next: Node

proc part1(input: list[int]): int =



proc main() =
  var input_list = input.split(" ")
  var int_list: seq[int] = @[125, 17]
  echo int_list
main()