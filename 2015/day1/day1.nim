# To run:
# nim r day1.nim

const input_file = "input.txt"

# Read input
import std/strutils

const input = staticRead(input_file).strip()

### Part 1

# Count the floors
var floor = 0

for c in input:
  if c == '(':
    floor += 1
  elif c == ')':
    floor -= 1

echo "Santa is on floor ", floor
# answer 138

### Part 2

floor = 0
for position, character in input:
    if character == '(':
        floor += 1
    if character == ')':
        floor -= 1
    
    # Check if basement
    if floor == -1:
        echo position+1 # Add +1 to position, since started from 0, not 1
        break
    
# answer 1771