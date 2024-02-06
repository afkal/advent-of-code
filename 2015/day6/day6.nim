# To run:
# nim r day6.nim

# Read input
import std/strutils

const input_file = "input.txt"
const input = staticRead(input_file).strip()
const lines = input.splitLines()

proc parse_line(line: string) =
    var words = line.split(" ")
    if words[0] == "turn":
        if words[1] == "on":
            echo "turn on " & words[2] & "-" & words[4]
        elif words[1] == "off":
            echo "turn off" & words[2] & "-" & words[4]
        else:
            echo "error"
    elif words[0] == "toggle":
        echo "toggle " & words[1] & "-" & words[3]

    #for word in words:
    #    echo word

for line in lines:
    #echo(line)
    parse_line(line)