# To run:
# nim r day2.nim

# Read input
import std/strutils
import std/algorithm
import std/sequtils

const input_file = "input.txt"
const input = staticRead(input_file).strip()
const lines = input.splitLines()

var total_area = 0
var total_ribbon = 0

# Iterate over lines
for line in lines:

    let dim: seq[int] = line.split('x').map(parseInt).sorted()

    total_area += (2*dim[0]*dim[1]+2*dim[1]*dim[2]+2*dim[2]*dim[0]+dim[0]*dim[1])
    total_ribbon += 2*dim[0]+2*dim[1]+dim[0]*dim[1]*dim[2]

echo(total_area)   # Part1: 1606483
echo(total_ribbon) # Part2: 3842356