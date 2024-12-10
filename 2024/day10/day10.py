test_data1 = """
0123
1234
8765
9876"""

test_data2 = """
1230432
5431345
3452543
6543456
7321127
8123438
9321239"""

test_data3 = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def get_input_data(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def get_matrix(data):
    # Change data from str to int
    data = data.strip().split('\n')
    data = [list(row) for row in data]
    matrix = []
    for row in data:
        matrix.append(list(row))
    for row in matrix:
        for i, value in enumerate(row):
            row[i] = int(value)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="")
        print()


def traverse(matrix, y, x, seed, trailheads=[]):
    """ Traverse matrix from x,y for incremental paths """
    if matrix[y][x] == 9:
        #print("Found path at: ", y, x)
        trailheads.append((y, x))
        #print("Trailheads: ", trailheads)
    if y > 0 and matrix[y-1][x] == seed+1:
        #print("At: (", y, x, ") Seed is: ", seed, "Going up")
        traverse(matrix, y-1, x, seed+1, trailheads)
    if y < len(matrix)-1 and matrix[y+1][x] == seed+1:
        #print("At: (", y, x, ") Seed is: ", seed, "Going down")
        traverse(matrix, y+1, x, seed+1, trailheads)
    if x > 0 and matrix[y][x-1] == seed+1:
        #print("At: (", y, x, ") Seed is: ", seed, "Going left")
        traverse(matrix, y, x-1, seed+1, trailheads)
    if x < len(matrix[0])-1 and matrix[y][x+1] == seed+1:
        #print("At: (", y, x, ") Seed is: ", seed, "Going right")
        traverse(matrix, y, x+1, seed+1, trailheads)

    # part1.  Return the number of unique trailheads
    #return len(set(trailheads))  # Return the length of unique trailheads

    # part2.  Return the total number of trailheads
    return len(trailheads)  # Return the length of unique trailheads


def scan_matrix(matrix):
    score = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                print("Starting at: ", i, j)
                trailheads = traverse(matrix, i, j, 0, [])
                print("Found trailheads: ", trailheads)
                score += trailheads
    return score
            

def part1(matrix):
    print("Analyzing matrix:")
    print_matrix(matrix)
    #trailheads = traverse(matrix, 0, 0, 0)
    #print("Trailheads: ", trailheads)
    score = scan_matrix(matrix)
    print("Score: ", score)


def main():
    matrix = get_matrix(get_input_data("input.txt"))
    #matrix = get_matrix(test_data3)
    part1(matrix)


if __name__ == '__main__':
    main()