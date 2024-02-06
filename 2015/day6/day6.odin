package main

import "core:os"
import "core:strings"
import "core:fmt"

read_file_by_lines_in_whole :: proc(filepath: string) -> []string {
	data, ok := os.read_entire_file(filepath, context.allocator)
	if !ok {
		// could not read file
		return []string{};
	}
	defer delete(data, context.allocator)

	it := string(data)
    lines := []string{};
	for line in strings.split_lines_iterator(&it) {
		fmt.print(line)
        lines = append(line);
	}
    return lines;
}

main :: proc() {
	fmt.println("Hellope!")

    // Read input file
    read_file_by_lines_in_whole("./input.txt")
}