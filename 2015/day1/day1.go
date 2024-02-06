package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

// Read the input file input.txt
// If the file exists, read the file and return the contents
// If the file does not exist, return an error
func readInput() (data string, err error) {
	// Get the current directory
	dir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	// Read the input file input.txt
	file := filepath.Join(dir, "input.txt")
	// Check if the file exists
	if _, err := os.Stat(file); os.IsNotExist(err) {
		return "", err
	}
	// Read the file
	dat, err := os.ReadFile(file)
	if err != nil {
		return "", err
	}
	// Convert the file contents to a string
	data = string(dat)
	return
}

func part1(input string) (floor int) {
	// Part 1
	// Loop through the input string
	// If the character is an open parenthesis, increment the floor
	// If the character is a close parenthesis, decrement the floor
	// Return the floor
	for _, c := range input {
		if c == '(' {
			floor++
		} else if c == ')' {
			floor--
		}
	}
	return
}

func part2(input string) (position int) {
	// Part 2
	// Loop through the input string
	// If the character is an open parenthesis, increment the floor
	// If the character is a close parenthesis, decrement the floor
	// If the floor is -1, return the position
	floor := 0
	for position, c := range input {
		if c == '(' {
			floor++
		} else if c == ')' {
			floor--
		}
		if floor == -1 {
			return position+1
		}
	}
	return
}

func main() {
	input, err := readInput()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part1(input)) // 138
	fmt.Println(part2(input)) // 1771


}