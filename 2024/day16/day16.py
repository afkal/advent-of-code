import time
import sys

sys.setrecursionlimit(10000)

test_input0 = """
######
#S...#
#.##.#
#.E..#
######
"""

test_input1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

test_input2= """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

sleep_time = 0.0


def get_input():
    with open("input.txt") as f:
        return f.read()
    

def parse_input(input):
    return [list(row) for row in input.strip().split("\n")]


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def find_start(matrix):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "S":
                return i, j
            


def traverse3(matrix, start, direction, score, sleep_time=0.0):
    """
    Traverse the matrix from start to end and return the lowest score
    Start is indicated by S
    End is indicated by E
    Walls are indicated by #
    Empty cells are indicated by .
    Score of each step is 1 point
    Score of each turn is 1000 points
    """

    stack = [(start, direction, score, set())]
    min_score = float('inf')

    while stack:
        (i, j), direction, score, visited = stack.pop()

        if matrix[i][j] == "E":
            min_score = min(min_score, score)
            continue

        visited.add((i, j, direction))

        # If score is already higher than the lowest score, skip
        if score >= min_score:
            continue

        matrix[i][j] = direction
        #ßprint("\n")
        #print_matrix(matrix)
        print("Current position: (", i, j, direction, ") Score: ", score, "/", min_score, end="\r")
        time.sleep(sleep_time)

        matrix[i][j] = " "

        if direction == ">":
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] != "#" and (i, j + 1, ">") not in visited:
                stack.append(((i, j + 1), ">", score + 1, visited.copy()))
            if i - 1 >= 0 and matrix[i - 1][j] != "#" and (i - 1, j, "^") not in visited:
                stack.append(((i - 1, j), "^", score + 1000, visited.copy()))
            if i + 1 < len(matrix) and matrix[i + 1][j] != "#" and (i + 1, j, "v") not in visited:
                stack.append(((i + 1, j), "v", score + 1000, visited.copy()))
        elif direction == "<":
            if j - 1 >= 0 and matrix[i][j - 1] != "#" and (i, j - 1, "<") not in visited:
                stack.append(((i, j - 1), "<", score + 1, visited.copy()))
            if i - 1 >= 0 and matrix[i - 1][j] != "#" and (i - 1, j, "^") not in visited:
                stack.append(((i - 1, j), "^", score + 1000, visited.copy()))
            if i + 1 < len(matrix) and matrix[i + 1][j] != "#" and (i + 1, j, "v") not in visited:
                stack.append(((i + 1, j), "v", score + 1000, visited.copy()))
        elif direction == "^":
            if i - 1 >= 0 and matrix[i - 1][j] != "#" and (i - 1, j, "^") not in visited:
                stack.append(((i - 1, j), "^", score + 1, visited.copy()))
            if j - 1 >= 0 and matrix[i][j - 1] != "#" and (i, j - 1, "<") not in visited:
                stack.append(((i, j - 1), "<", score + 1000, visited.copy()))
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] != "#" and (i, j + 1, ">") not in visited:
                stack.append(((i, j + 1), ">", score + 1000, visited.copy()))
        elif direction == "v":
            if i + 1 < len(matrix) and matrix[i + 1][j] != "#" and (i + 1, j, "v") not in visited:
                stack.append(((i + 1, j), "v", score + 1, visited.copy()))
            if j - 1 >= 0 and matrix[i][j - 1] != "#" and (i, j - 1, "<") not in visited:
                stack.append(((i, j - 1), "<", score + 1000, visited.copy()))
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] != "#" and (i, j + 1, ">") not in visited:
                stack.append(((i, j + 1), ">", score + 1000, visited.copy()))

    return min_score


scores = []

def traverse2(matrix, start, direction, score, visited):
    """
    Traverse the matrix from start to end and return the lowest score
    Start is indicated by S
    End is indicated by E
    Walls are indicated by #
    Empty cells are indicated by .
    Score of each step is 1 point
    Score of each turn is 1000 points
    """

    visited = visited.copy()

    i, j = start

    if matrix[i][j] == "E":
        return score

    visited.add((i, j, direction))

    matrix[i][j] = direction
    print("\n")
    print_matrix(matrix)
    print("Current position: (", i, j, direction, ") Score: ", score, end="\r")
    time.sleep(sleep_time) 
    
    #scores = []

    if direction == ">":
        if matrix[i][j+1] != "#" and (i, j+1, direction) not in visited:
            matrix[i][j] = " "
            scores.append(traverse2(matrix, (i, j+1), ">", score+1, visited))
        if matrix[i-1][j] != "#" and (i, j, "^") not in visited:
            scores.append(traverse2(matrix, (i, j), "^", score+1000, visited))
        if matrix[i+1][j] != "#" and (i, j, "v") not in visited:
            scores.append(traverse2(matrix, (i, j), "v", score+1000, visited))
    if direction == "<":
        if matrix[i][j-1] != "#" and (i, j-1, direction) not in visited:
            matrix[i][j] = " "
            scores.append(traverse2(matrix, (i, j-1), "<", score+1, visited))
        if matrix[i-1][j] != "#" and (i, j, "^") not in visited:
            scores.append(traverse2(matrix, (i, j), "^", score+1000, visited))
        if matrix[i+1][j] != "#" and (i, j, "v") not in visited:
            scores.append(traverse2(matrix, (i, j), "v", score+1000, visited))
    if direction == "^":
        if matrix[i-1][j] != "#" and (i-1, j, direction) not in visited:
            matrix[i][j] = " "
            scores.append(traverse2(matrix, (i-1, j), "^", score+1, visited))
        if matrix[i][j+1] != "#" and (i, j, ">") not in visited:
            scores.append(traverse2(matrix, (i, j), ">", score+1000, visited))
        if matrix[i][j-1] != "#" and (i, j, "<") not in visited:
            scores.append(traverse2(matrix, (i, j), "<", score+1000, visited))
    if direction == "v":
        if matrix[i+1][j] != "#" and (i+1, j, direction) not in visited:
            matrix[i][j] = " "
            scores.append(traverse2(matrix, (i+1, j), "v", score+1, visited))
        if matrix[i][j+1] != "#" and (i, j, ">") not in visited:
            scores.append(traverse2(matrix, (i, j), ">", score+1000, visited))
        if matrix[i][j-1] != "#" and (i, j, "<") not in visited:
            scores.append(traverse2(matrix, (i, j), "<", score+1000, visited))
    
    # If no more moves are possible, return the dead end score (1000000)
    #if not scores:
    matrix[i][j] = "."
    return 1000000
    
    # Routes find to the end return the scores
    #return min(scores)

points_until_end = [float('inf')]
succesfull_routes = []
min_scores = []

def traverse(matrix, start, direction, score, visited):
    """
    Traverse the matrix from start to end and return the lowest score
    Start is indicated by S
    End is indicated by E
    Walls are indicated by #
    Empty cells are indicated by .
    Score of each step is 1 point
    Score of each turn is 1000 points
    """

    # If score is already higher than the lowest score, skip
    if points_until_end and score > min(points_until_end):
        return float('inf')

    scores = []
    i, j = start

    # Check if current position is visited with lower score
    if min_scores[i][j][direction] >= score:
        min_scores[i][j][direction] = score
    else:
        #print("Already visited with lower score:", min_scores[i][j], "Current score:", score)
        return float('inf')


    if matrix[i][j] == "E":
        points_until_end.append(score)
        succesfull_routes.append(visited)
        return score

    # Never append E to visited
    visited.add((i, j, direction))

    matrix[i][j] = direction
    #print("\n")
    #print_matrix(matrix)
    print("Current position: (", i, j, direction, ") Score: ", score, "/", min(points_until_end), "     ",end="\r")
    time.sleep(sleep_time)

    matrix[i][j] = " "
    
    if direction == ">":
        if matrix[i][j+1] != "#" and (i, j+1, direction) not in visited:

            scores.append(traverse(matrix, (i, j+1), ">", score+1, visited.copy()))
        if (i, j, "^") not in visited and matrix[i-1][j] != "#":
            scores.append(traverse(matrix, (i, j), "^", score+1000, visited.copy()))
        if (i, j, "v") not in visited and matrix[i+1][j] != "#":
            scores.append(traverse(matrix, (i, j), "v", score+1000, visited.copy()))
    if direction == "<":
        if matrix[i][j-1] != "#" and (i, j-1, direction) not in visited:
            scores.append(traverse(matrix, (i, j-1), "<", score+1, visited.copy()))
        if (i, j, "^") not in visited and matrix[i-1][j] != "#":
            scores.append(traverse(matrix, (i, j), "^", score+1000, visited.copy()))
        if (i, j, "v") not in visited and matrix[i+1][j] != "#":
            scores.append(traverse(matrix, (i, j), "v", score+1000, visited.copy()))
    if direction == "^":
        if matrix[i-1][j] != "#" and (i-1, j, direction) not in visited:
            scores.append(traverse(matrix, (i-1, j), "^", score+1, visited.copy()))
        if (i, j, ">") not in visited and matrix[i][j+1] != "#":
            scores.append(traverse(matrix, (i, j), ">", score+1000, visited.copy()))
        if (i, j, "<") not in visited and matrix[i][j-1] != "#":
            scores.append(traverse(matrix, (i, j), "<", score+1000, visited.copy()))
    if direction == "v":
        if matrix[i+1][j] != "#" and (i+1, j, direction) not in visited:
            scores.append(traverse(matrix, (i+1, j), "v", score+1, visited.copy()))
        if (i, j, ">") not in visited and matrix[i][j+1] != "#":
            scores.append(traverse(matrix, (i, j), ">", score+1000, visited.copy()))
        if (i, j, "<") not in visited and matrix[i][j-1] != "#":
            scores.append(traverse(matrix, (i, j), "<", score+1000, visited.copy()))
        
    # If no more moves are possible, return the dead end score (1000000)
    if not scores:
        matrix[i][j] = "."
        return float('inf')
    
    return min(scores)


def print_successfull_routes(matrix, succesfull_routes):
    for route in succesfull_routes:
        for i, j, direction in route:
            matrix[i][j] = direction
        print("\n")
        print_matrix(matrix)


def part1(input):
    global min_scores
    input = parse_input(input)
    print_matrix(input)
    start = find_start(input)
    for i in range(len(input)):
        min_scores.append([])
        for j in range(len(input[0])):
            min_scores[i].append({"<": float('inf'), ">": float('inf'), "^": float('inf'), "v": float('inf')})
    print("Start: ", start)
    direction = ">"
    score = 0
    score = traverse(input, start, direction, score, visited=set())
    #score = traverse2(input, start, direction, score, visited=set())
    #score = traverse3(input, start, direction, score)
    print("\n")
    print("Scores until end: ", score)
    #print("Lowest score: ", min(scores))
    print("Points until end: ", points_until_end)
    #print_successfull_routes(input, succesfull_routes)


def main():
    input = get_input()
    #part1(test_input2)
    part1(input)


if __name__ == "__main__":
    main()

# 11037 / 11048
# 7029 / 7036
