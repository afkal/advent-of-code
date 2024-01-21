# To run:
# nim r day5.nim

# Read input
import std/strutils

const input_file = "input.txt"
const input = staticRead(input_file).strip()
const lines = input.splitLines()

# Test vectors
#const lines = @["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
#const lines = @["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]

const vowels = "aeiou"
var nice_count = 0

func is_vowel(character: char): bool =
    if character in vowels: return true
    return false

func contains_vowels(input: string) : bool =
    var count = 0
    for character in input:
        if is_vowel(character):
            count += 1
        
    if count > 2: return true
    return false

func contains_double_letter(input: string): bool =
    var previous = ' '
    for character in input:
        if character == previous: return true
        previous = character
    return false

func contains_not_allowed(input: string): bool =
    if "ab" in input: return true
    if "cd" in input: return true
    if "pq" in input: return true
    if "xy" in input: return true
    return false

# Part 1:
for line in lines:
    # Iterate line
    #for char in line:
    #echo line
    if not contains_vowels(line):
        continue
    if not contains_double_letter(line):
        continue
    if contains_not_allowed(line):
        continue
    #echo(line & " is nice!")
    nice_count += 1

echo("Part 1: " & $nice_count)


proc contains_pair_of_two(input: string): bool =
    # eg. xyxy
    var previous = ' '
    for index, current in input:
        #echo "index: ", index
        #echo "previous + current: ", previous & current
        #echo "remaining input: ", input[index+1 .. len(input)-1]
        if previous & current in input[index+1 .. len(input)-1]:
            #echo "found pair of two! ", previous & current, " in ", input[index+1 .. len(input)-1]
            return true
        previous = current

    return false


func contains_one_letter_between(input: string): bool =
    var before_previous = ' '
    var previous = ' '
    for current in input:
        if current == before_previous:
            return true
        before_previous = previous
        previous = current
    return false

# Part 2:
nice_count = 0
for line in lines:
    # Iterate line
    #for char in line:
    #echo line
    if not contains_pair_of_two(line):
        continue
    if not contains_one_letter_between(line):
        continue
    #echo(line & " is nice!")
    nice_count += 1

echo("Part 2: " & $nice_count)