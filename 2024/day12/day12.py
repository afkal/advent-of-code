test_input1 = """
AAAA
BBCD
BBCC
EEEC
"""

test_input2 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

test_input3 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

test_input4 = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""


visited = []

def get_input_data(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read().strip()
    return data


def to_matrix(data):
    data = data.strip().split('\n')
    matrix = []
    for row in data:
        matrix.append(list(row))
    return matrix


def print_matrix(matrix):
    for row in matrix:
        row = "".join(row)
        print(row)


def check_corners(matrix, y, x):
    """ Calculate corners """
    debug=False

    # Add cells around the matrix to avoid out of bounds
    # matrix.insert(0, ["#"]*len(matrix[0]))
    # matrix.append(["#"]*len(matrix[0]))
    # for i, _ in enumerate(matrix):
    #     matrix[i].insert(0, "#")
    #     matrix[i].append("#")

    matrix2 = []
    matrix2.append(["#"]*(len(matrix[0])+2))
    for row in matrix:
        matrix2.append(["#"] + row + ["#"])
    matrix2.append(["#"]*(len(matrix[0])+2))
    matrix = matrix2
    
    x += 1
    y += 1

    #print_matrix(matrix)
    if debug:
        print("Checking corners for: ", matrix[y][x], "at", y, x)
    corners = 0


    # Outside corners
    if matrix[y-1][x] != matrix[y][x] and matrix[y][x-1] != matrix[y][x]:
        if debug:
            print("Top left corner")
        corners += 1
    if matrix[y-1][x] != matrix[y][x] and matrix[y][x+1] != matrix[y][x]:
        if debug:
            print("Top right corner")
        corners += 1
    if matrix[y+1][x] != matrix[y][x] and matrix[y][x-1] != matrix[y][x]:
        if debug:
            print("Bottom left corner")
        corners += 1
    if matrix[y+1][x] != matrix[y][x] and matrix[y][x+1] != matrix[y][x]:
        if debug:
            print("Bottom right corner")
        corners += 1

    # Inside corners
    if matrix[y-1][x] == matrix[y][x] and matrix[y][x+1] == matrix[y][x] and matrix[y-1][x+1] != matrix[y][x]:
        if debug:
            print("Top right inside corner")
        corners += 1
    if matrix[y-1][x] == matrix[y][x] and matrix[y][x-1] == matrix[y][x] and matrix[y-1][x-1] != matrix[y][x]:
        if debug:
            print("Top left inside corner")
        corners += 1
    if matrix[y+1][x] == matrix[y][x] and matrix[y][x+1] == matrix[y][x] and matrix[y+1][x+1] != matrix[y][x]:
        if debug:
            print("Bottom right inside corner")
        corners += 1
    if matrix[y+1][x] == matrix[y][x] and matrix[y][x-1] == matrix[y][x] and matrix[y+1][x-1] != matrix[y][x]:
        if debug:
            print("Bottom left inside corner")
        corners += 1
    return corners


def traverse(matrix, y, x, area, perimeter, corners):
    """ Traverse matrix from x,y for incremental paths """
    if (y, x) in visited:
        return area, perimeter, corners

    # Add cell to visited
    visited.append((y, x))

    # Calculate perimeter
    if y > 0 and matrix[y-1][x] != matrix[y][x]:
        perimeter += 1
    if y < len(matrix)-1 and matrix[y+1][x] != matrix[y][x]:
        perimeter += 1
    if x > 0 and matrix[y][x-1] != matrix[y][x]:
        perimeter += 1
    if x < len(matrix[0])-1 and matrix[y][x+1] != matrix[y][x]:
        perimeter += 1
    if x == 0:
        perimeter += 1
    if x == len(matrix[0])-1:
        perimeter += 1
    if y == 0:
        perimeter += 1
    if y == len(matrix)-1:
        perimeter += 1
    #print("Perimeter: ", perimeter)

    # Check if we are in a corner
    corners += check_corners(matrix, y, x)

    #print("Corners: ", corners)

    #Increase area
    area += 1

    # Add cell to visited
    visited.append((y, x))

    # Check if we can go up, down, left or right
    if y < len(matrix)-1 and matrix[y+1][x] == matrix[y][x]:
        #print("At: (", y, x, ") Going down")
        area, perimeter, corners = traverse(matrix, y+1, x, area, perimeter, corners)
    
    if y > 0 and matrix[y-1][x] == matrix[y][x]:
        #print("At: (", y, x, ") Going up")
        area, perimeter, corners =  traverse(matrix, y-1, x, area, perimeter, corners)

    if x > 0 and matrix[y][x-1] == matrix[y][x]:
        #print("At: (", y, x, ") Going left")
        area, perimeter, corners =  traverse(matrix, y, x-1, area, perimeter, corners)

    if x < len(matrix[0])-1 and matrix[y][x+1] == matrix[y][x]:
        #print("At: (", y, x, ") Going right")
        area, perimeter, corners =  traverse(matrix, y, x+1, area, perimeter, corners)

    return area, perimeter, corners


def part1(data):
    """ Loop through the matrix """
    #area, value = traverse(data, 0, 0, 0, 0)
    #print(area, value)
    total_price = 0
    for i, row in enumerate(data):
         for j, value in enumerate(row):
            if (i, j) in visited:
                continue
            area, perimeter, corners = traverse(data, i, j, 0, 0, 0)
            print(value, i, j, end=" ")
            print("Area:", area, "Perimeter", perimeter, "Corners", corners, "Price:", area*perimeter)
            # part 1.
            #total_price += area*perimeter
            # part 2.
            total_price += area*corners
         print()
    return total_price


def main():
    data = get_input_data("input.txt")
    #data = test_input2
    data = to_matrix(data)
    result = part1(data)
    print(result)


# Test cases
def test_corners():
    data = to_matrix(test_input1)
    print(check_corners(data, 2, 2))
    #assert check_corners(data, 0, 0) == 2


if __name__ == "__main__":
    #test_corners()
    #exit()
    main()



