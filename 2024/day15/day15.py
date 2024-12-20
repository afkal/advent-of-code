import time

test_input0 = """
###########
#....@....#
#.........#
#.........#
#.O.OOO...#
#....O....#
#.........#
#.........#
###########
 
vvvvvvvvvvv"""

test_input1 = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

test_input2= """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""


def get_input():
    with open("input.txt") as f:
        return f.read()
    

def parse_input(input_str):
    matrix = []
    command_lines = []
    lines = input_str.strip().split("\n")
    lines = [list(line) for line in lines]
    for line in lines:
        if line == []:
            continue
        if line[0] == "#":
            matrix.append(line)
        else:
            command_lines += line

    commands = "".join(command_lines)

    return matrix, commands


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def find_start(matrix):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "@":
                return i, j
    return None


def find_boxes(matrix):
    boxes = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "O":
                boxes.append((i, j))
    return boxes


def try_to_move_boxes(matrix, i, j, direction):
    """
    Try to move boxes in the direction specified by the direction parameter.
    Move is successful if there is a free space in the direction.
    Free space is denoted by a "." character.
    If there is a box in the way, the box is moved in the same direction.
    If there is a wall in the way, the move is not possible.
    Returns True if the move was successful, False otherwise.
    """

    # Scan right for a free space
    if direction == ">":
        for k in range(j+1, len(matrix[0])):
            if matrix[i][k] == "O":
                continue
            if matrix[i][k] == "#":
                break
            if matrix[i][k] == ".":
                # Move boxes to the right
                print(f"Moving {k-j} boxes to the right from position ({i},{j}) to position ({i}, {k})")
                matrix[i][j] = "."
                for l in range(j+1, k+1):
                    matrix[i][l] = "O"
                return True
    if direction == "<":
        for k in range(j-1, -1, -1):
            if matrix[i][k] == "O":
                continue
            if matrix[i][k] == "#":
                break
            if matrix[i][k] == ".":
                # Move boxes to the left
                print(f"Moving {j-k} boxes to the left from position ({i},{j}) to position ({i}, {k})")
                matrix[i][j] = "."
                for l in range(k, j):
                    matrix[i][l] = "O"
                return True
    if direction == "^":
        for k in range(i-1, -1, -1):
            if matrix[k][j] == "O":
                continue
            if matrix[k][j] == "#":
                break
            if matrix[k][j] == ".":
                # Move boxes up
                print(f"Moving {i-k} boxes up from position ({i},{j}) to position ({k}, {j})")
                matrix[i][j] = "."
                for l in range(k, i):
                    matrix[l][j] = "O"
                return True
    if direction == "v":
        for k in range(i+1, len(matrix)):
            if matrix[k][j] == "O":
                continue
            if matrix[k][j] == "#":
                break
            if matrix[k][j] == ".":
                # Move boxes down
                print(f"Moving {k-i} boxes down from position ({i},{j}) to position ({k}, {j})")
                matrix[i][j] = "."
                for l in range(i+1, k+1):
                    matrix[l][j] = "O"
                return True
    return False

def move_robot(matrix, start, command):
    i, j = start
    if command == "<":
        if j > 0 and matrix[i][j-1] != "#":
            if matrix[i][j-1] == "O":
                if try_to_move_boxes(matrix, i, j-1, "<"):
                    matrix[i][j] = "."
                    matrix[i][j-1] = "@"
                    return i, j-1
            else:
                matrix[i][j] = "."
                matrix[i][j-1] = "@"
                return i, j-1
    elif command == ">":
        if j < len(matrix[0])-1 and matrix[i][j+1] != "#":
            if matrix[i][j+1] == "O":
                if try_to_move_boxes(matrix, i, j+1, ">"):
                    matrix[i][j] = "."
                    matrix[i][j+1] = "@"
                    return i, j+1
            else:
                matrix[i][j] = "."
                matrix[i][j+1] = "@"
                return i, j+1
    elif command == "^":
        if i > 0 and matrix[i-1][j] != "#":
            if matrix[i-1][j] == "O":
                if try_to_move_boxes(matrix, i-1, j, "^"):
                    matrix[i][j] = "."
                    matrix[i-1][j] = "@"
                    return i-1, j
            else:
                matrix[i][j] = "."
                matrix[i-1][j] = "@"
                return i-1, j
    elif command == "v":
        if i < len(matrix)-1 and matrix[i+1][j] != "#":
            if matrix[i+1][j] == "O":
                if try_to_move_boxes(matrix, i+1, j, "v"):
                    matrix[i][j] = "."
                    matrix[i+1][j] = "@"
                    return i+1, j
            else:
                matrix[i][j] = "."
                matrix[i+1][j] = "@"
                return i+1, j
    return start


def calculate_gps_coordinates(matrix):
    gps_checksum = 0
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "O":
                gps_checksum += i*100+j
    return gps_checksum


def part1(matrix, commands):
    start = find_start(matrix)
    if start is None:
        return None
    boxes = find_boxes(matrix)
    print("Boxes:", boxes)
    print("Starting position:", start)
    for command in commands:
        start = move_robot(matrix, start, command)
        print_matrix(matrix)
        print("Moved robot to:", start)
        time.sleep(0.5)
    gps_checksum=calculate_gps_coordinates(matrix)
    print
    print("GPS checksum:", gps_checksum)


def scale_matrix(matrix):
    """ Scale the matrix twice as wide """
    new_matrix = []
    for row in matrix:
        new_row = []
        for cell in row:
            if cell == "@":
                new_row.append(cell)
                new_row.append(".")
            if cell == "O":
                new_row.append("[")
                new_row.append("]")
            if cell == ".":
                new_row.append(".")
                new_row.append(".")
            if cell == "#":
                new_row.append("#")
                new_row.append("#")
        new_matrix.append(new_row)
    return new_matrix


def try_to_move_boxes_left(matrix, i, j):
    for k in range(j-1, -1, -1):
        if matrix[i][k] == "[" or matrix[i][k] == "]":
            continue
        if matrix[i][k] == "#":
            break
        if matrix[i][k] == ".":
            # Move boxes to the left
            print(f"Moving {(j-k)/2} large boxes to the left from position ({i},{j}) to position ({i}, {k})")
            matrix[i][j] = "."
            for l in range(k, j, 2):
                matrix[i][l] = "["
                matrix[i][l+1] = "]"
            return True
    return False


def try_to_move_boxes_right(matrix, i, j):
    for k in range(j+1, len(matrix[0])):
        if matrix[i][k] == "[" or matrix[i][k] == "]":
            continue
        if matrix[i][k] == "#":
            break
        if matrix[i][k] == ".":
            # Move boxes to the right
            print(f"Moving {(j-k)/2} large boxes to the right from position ({i},{j}) to position ({i}, {k})")
            matrix[i][j] = "."
            for l in range(j+1, k+1, 2):
                matrix[i][l] = "["
                matrix[i][l+1] = "]"
            return True
    return False


def try_to_move_boxes_up(matrix, i, j):
    for k in range(i-1, -1, -1):
        if matrix[k][j] == "[" or matrix[k][j] == "]":
            continue
        if matrix[k][j] == "#":
            break
        if matrix[k][j] == ".":
            # Move boxes up
            print(f"Moving {(i-k)/2} large boxes up from position ({i},{j}) to position ({k}, {j})")
            matrix[i][j] = "."
            for l in range(k, i, 2):
                matrix[l][j] = "["
                matrix[l+1][j] = "]"
            return True
    return False


def try_to_move_boxes_down(matrix, i, j):
    for k in range(i+1, len(matrix)):
        if matrix[k][j] == "[" or matrix[k][j] == "]":
            continue
        if matrix[k][j] == "#":
            break
        if matrix[k][j] == ".":
            # Move boxes down
            print(f"Moving {(k-i)/2} large boxes down from position ({i},{j}) to position ({k}, {j})")
            matrix[i][j] = "."
            for l in range(i+1, k+1, 2):
                matrix[l][j] = "["
                matrix[l+1][j] = "]"
            return True
    return False


def move_robot2(matrix, start, command):
    i, j = start
    if command == "<":
        if matrix[i][j-1] == "#":
            return start
        if matrix[i][j-1] == ".":
            matrix[i][j] = "."
            matrix[i][j-1] = "@"
            return i, j-1
        if matrix[i][j-1] == "]":
            if try_to_move_boxes_left(matrix, i, j-1):
                matrix[i][j] = "."
                matrix[i][j-1] = "@"
                return i, j-1
    if command == ">":
        if matrix[i][j+1] == "#":
            return start
        if matrix[i][j+1] == ".":
            matrix[i][j] = "."
            matrix[i][j+1] = "@"
            return i, j+1
        if matrix[i][j+1] == "[":
            if try_to_move_boxes_right(matrix, i, j+1):
                matrix[i][j] = "."
                matrix[i][j+1] = "@"
                return i, j+1
    if command == "^":
        if matrix[i-1][j] == "#":
            return start
        if matrix[i-1][j] == ".":
            matrix[i][j] = "."
            matrix[i-1][j] = "@"
            return i-1, j
        if matrix[i-1][j] == "]" or matrix[i-1][j] == "[":
            if try_to_move_boxes_up(matrix, i-1, j):
                matrix[i][j] = "."
                matrix[i-1][j] = "@"
                return i-1, j
    if command == "v":
        if matrix[i+1][j] == "#":
            return start
        if matrix[i+1][j] == ".":
            matrix[i][j] = "."
            matrix[i+1][j] = "@"
            return i+1, j
        if matrix[i+1][j] == "[" or matrix[i+1][j] == "]":
            if try_to_move_boxes_down(matrix, i+1, j):
                matrix[i][j] = "."
                matrix[i+1][j] = "@"
                return i+1, j
            
    return start


def part2(matrix, commands):
    matrix = scale_matrix(matrix)
    print_matrix(matrix)
    start = find_start(matrix)
    if start is None:
        return None
    for command in commands:
        start = move_robot2(matrix, start, command)
        print_matrix(matrix)
        print("Moved robot to:", start, end="\r")
        time.sleep(0.5)


def main():
    #input_str = get_input()
    input_str = test_input0
    matrix, commands = parse_input(input_str)
    
    # Part 1
    # print_matrix(matrix)
    # print(commands)
    #part1(matrix, commands)

    # Part 2
    part2(matrix, commands)


if __name__ == "__main__":
    main()