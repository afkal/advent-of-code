# To run:
# nim r day3.nim

# Read input
import std/strutils
import tables

const input_file = "input.txt"
const input = staticRead(input_file).strip()
const lines = input.splitLines()

# Test vectors
#const lines = @["^>v<"]

# Let's work with imaginary matrix
#
# side_length = 6
# mid_point = 36 / 2 = 18
#
#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25


# lets create an imaginary matrix of dimension 5000 x 5000
const side_lenght = 50000
const start_position = 130000

var position = 13000000

# Hashmap of visited positions
var visited = initTable[int, int]() # hashmap of visited places
visited[position] = 1 # starting position is visited always

# Part 1:
for line in lines:
    # Iterate line
    for char in line:
        case char:
        of '>':
            position += 1
        of '<':
            position -= 1
        of '^':
            position -= side_lenght
        of 'v':
            position += side_lenght
        else:
            continue

        if(visited.hasKey(position)):
            visited[position] += 1
        else:
            visited[position] =1

echo("Part 1: ", visited.len) # Part1: 2572

### Part 2:

var santa_position, r_santa_position = 13000000 # both santas start at same position
visited = initTable[int, int]() # hashmap of visited places
visited[santa_position] = 1 # starting position is visited always
var santa = true
for line in lines:
    # Iterate line
    for index, char in line:

        #check index
        if index mod 2 == 0:
            santa = true
        else:
            santa = false
        case char:
        of '>':
            if santa:
                santa_position += 1
            else:
                r_santa_position += 1
        of '<':
            if santa:
                santa_position -= 1
            else:
                r_santa_position -= 1
        of '^':
            if santa:
                santa_position -= side_lenght
            else:
                r_santa_position -= side_lenght
        of 'v':
            if santa:
                santa_position += side_lenght
            else:
                r_santa_position += side_lenght
        else:
            continue

        #echo("    santa: ", santa_position)
        #echo("robosanta: ", r_santa_position)
        if(visited.hasKey(santa_position)):
            visited[santa_position] += 1
        else:
            visited[santa_position] = 1

        if(visited.hasKey(r_santa_position)):
            visited[r_santa_position] += 1
        else:
            visited[r_santa_position] = 1

#echo("Visited", visited)
echo("Part 2: ", visited.len) # Part2: 2572