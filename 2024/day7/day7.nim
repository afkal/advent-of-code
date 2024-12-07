import strutils, sequtils

let test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


proc echo(input: string) =
  echo input

proc parse_input(input: string): seq[(int, seq[int])] =
    result = @[]
    for line in input.splitLines:
        let parts = line.split(": ")
        let key = parts[0].parseInt
        let values = parts[1].split(" ").mapIt(it.parseInt)
        result.add((key, values))


proc check_if_valid(key: int, values: seq[int] ): bool =
    result = false
    # iterate over values
    for value in values:
        if key % value == 0:
            result = true
    return result


proc part1(data: seq[(int, seq[int])]): int =
    result = 0
    for item in data:
        let key = item[0]
        let values = item[1]
        let result = check_if_valid(key, values)
    return result


proc main() =
    let test_data = parse_input(test_input)
    let result = part1(test_data)
    echo result

main()