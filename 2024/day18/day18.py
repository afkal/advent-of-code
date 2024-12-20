test_input0 = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def parse_input(input):
    return input.split("\n")


def print_grid(grid):
    for row in grid:
        print("".join(row))


def populate_grid(input, size, bytes):
    grid = [['.' for i in range(size)] for j in range(size)]
    for i, line in enumerate(input.split("\n")):
        if i>=bytes:
            break
        x, y = line.split(",")
        grid[int(y)][int(x)] = '#'
    grid[size-1][size-1] = 'E'

    # Add borders around the grid
    for i in range(size):
        grid[i].insert(0, '#')
        grid[i].append('#')

    grid.insert(0, ['#' for i in range(size+2)])
    grid.append(['#' for i in range(size+2)])
    grid[1][1] = 'S'

    return grid


def find_shortest_path(grid, start, end):
    """
    Shortest path using BFS
    
    :param grid:
    :param start:
    :param end:
    :return: path length
    """

    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), dist = queue.pop(0)
        if (x, y) == end:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if grid[new_y][new_x] == '#':
                continue
            queue.append(((new_x, new_y), dist + 1))
    return -1



def part1(input):
    print("Part 1")
    #print(input)

    input = open("input.txt").read().strip()
    grid = populate_grid(input, 71, 1024)
    start = (1, 1)
    end = (71, 71)

    print(grid[71][71])

    # input = test_input0
    # grid = populate_grid(input, 7, 12)
    # print_grid(grid)
    # start = (1, 1)
    # end = (7, 7)
    # print(grid[1][1])
    
    print(find_shortest_path(grid, start, end))


    # Part 2

    for i in range(len(input)):
        grid = populate_grid(input, 71, i)
        start = (1, 1)
        end = (71, 71)
        path = find_shortest_path(grid, start, end)
        if path == -1:
            print("Path blocked at byte", i)
            break
        else:
            print("Path length at byte", i, ":", path)


def main():
    print("Day 18")

    # Part 1
    part1(input)

    # Part 2


if __name__ == "__main__":
    main()