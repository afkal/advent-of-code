# To run:
# nim r day4.nim

# Read input
import std/strutils
import md5


# Input
const input = "iwrupvqb"
#const input = "abcdef"

#let hash = getMD5("pqrstuv1048970")

var number = 1000000
var hash = ""
while number < 1_000_000_000:
    echo(input & $number)
    hash = getMD5(input & $number)
    if(hash[0..5] == "000000"): # eg. 000001dbbfa3a5c83a2d506429c7b00e
        echo("found! " & $number)
        break
    number += 1

echo hash
echo number # Part 2: 9958218