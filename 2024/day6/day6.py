import time

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


test_input2 = """...........#.....#......
...................#....
...#.....##.............
......................#.
..................#.....
..#.....................
....................#...
........................
.#........^.............
..........#..........#..
..#.....#..........#....
........#.....#..#......"""

test_input3 = """###
..#
^##"""

test_input4 = """##..
...#
....
^.#."""

test_input5 = """#.....
.....#
^.#..#
....#."""

class Grid:
    map = None
    visited_positions = []


    def __init__(self, map):
        self.map = map
        self.visited_positions = []


    def print(self):
        for row in self.map:
            print("".join(row))


    def find_starting_position(self):
        for row in self.map:
            if "^" in row:
                return (self.map.index(row), row.index("^"))
        return None
    

    def is_in_unique_visited_positions(self, position):
        positions = [position for position, _ in self.visited_positions]
        if position in positions:
            return True
        return False
    

    def get_unique_visited_positions(self):
        ''' Get the unique visited positions - do not care about the direction '''
        positions = [position for position, _ in self.visited_positions]
        return list(set(positions))
    

    def add_to_visited_positions(self, position, direction):
        ''' Add the position and direction to the visited positions '''
        self.visited_positions.append((position, direction))


    def is_in_visited_positions(self, position, direction):
        ''' Check if the position and direction is in the visited positions '''
        if (position, direction) in self.visited_positions:
            return True
        return False


    def paint_position(self, position, direction):
        ''' Paint the position with the direction '''
        if self.is_in_unique_visited_positions(position):
            self.map[position[0]][position[1]] = "+"
        elif direction == "up" or direction == "down":
            self.map[position[0]][position[1]] = "|"
        elif direction == "left" or direction == "right":
            self.map[position[0]][position[1]] = "-"
        else:
            self.map[position[0]][position[1]] = "X"


    def is_wall(self, position):
        ''' Check if the position is a wall '''
        if self.map[position[0]][position[1]] == "#" or self.map[position[0]][position[1]] == "O":
            return True
        return False


    def count_path(self):
        count = 0
        for row in self.map:
            for col in row:
                if col == "X":
                    count += 1
        return count
    

    def add_obstacle(self, position):
        self.map[position[0]][position[1]] = "O"


def get_input():
    with open('input.txt') as f:
        input = f.read()
    return input


def create_grid(input):
    lines = input.split("\n")
    lines = [x.strip() for x in lines]
    grid = []
    for line in lines:
        grid.append([x for x in line])
    return grid


def find_starting_position(grid):
    for row in grid:
        if "^" in row:
            return (grid.index(row), row.index("^"))
    return None


def patrol(grid, pos, dir):
    ''' Patrol Guard in the grid until reaches the edge of the grid
     or a position that has already been visited in the same direction,
     which means that the guard is in a loop
     
     Returns the number of positions visited of zero if the guard is in a loop
     '''
    
    
    while pos[0]> 0 and pos[1] > 0 and pos[0] < len(grid.map)-1 and pos[1] < len(grid.map[0])-1:  
        if dir == "up":
            if grid.is_wall((pos[0]-1,pos[1])):
                if grid.is_wall((pos[0], pos[1]+1)):
                    dir = "down"
                    #pos = (pos[0]+1, pos[1])
                else:
                    dir = "right"
                    pos = (pos[0], pos[1]+1)
            else:
                pos = (pos[0]-1, pos[1])
        elif dir == "right":
            if grid.is_wall((pos[0], pos[1]+1)):
                if grid.is_wall((pos[0]+1, pos[1])):
                    dir = "left"
                    #pos = (pos[0], pos[1]-1)
                else:
                    dir = "down"
                    pos = (pos[0]+1, pos[1])
            else:
                pos = (pos[0], pos[1]+1)
        elif dir == "down":
            if grid.is_wall((pos[0]+1, pos[1])):
                if grid.is_wall((pos[0], pos[1]-1)):
                    dir = "up"
                    #pos = (pos[0]-1, pos[1])
                else:
                    dir = "left"
                    pos = (pos[0], pos[1]-1)
            else:
                pos = (pos[0]+1, pos[1])
        elif dir == "left":
            if grid.is_wall((pos[0], pos[1]-1)):
                if grid.is_wall((pos[0]-1, pos[1])):
                    dir = "right"
                    #pos = (pos[0], pos[1]+1)
                else:
                    dir = "up"
                    pos = (pos[0]-1, pos[1])
            else:
                pos = (pos[0], pos[1]-1)

        # Check if the position is in the visited positions
        if grid.is_in_visited_positions(pos, dir):
            # Loop detected - return 0
            return 0
        else:
            # Add the new position and direction to the visited positions
            grid.paint_position(pos, dir)
            grid.add_to_visited_positions(pos, dir)
            #grid.print()

    #print("Path count: ", grid.count_path())
    #print("Visited positions size: ", len(grid.visited_positions))
    #print("End of patrol")
    print("Exited at position: ", pos, end="\r")
    return len(grid.get_unique_visited_positions())


def part1(input):
    grid = Grid(create_grid(input))
    position = grid.find_starting_position()
    direction = "up"
    grid.paint_position(position, direction)
    
    # Hack add obstacle
    #grid.add_obstacle((0, 1))

    grid.print()
    pathpoints = patrol(grid, position, direction)
    print("Path points: ", pathpoints)

    grid = Grid(create_grid(input))
    position = grid.find_starting_position()
    direction = "up"
    pathpoints = patrol(grid, position, direction)
    grid.print()
    print("Path points: ", pathpoints)


def part2(input):

    # Get initial route with no obstacles
    grid = Grid(create_grid(input))
    initial_position = grid.find_starting_position()
    direction = "up" # Set direction
    grid.paint_position(initial_position, direction) # Paint starting position
    pathpoints = patrol(grid, initial_position, direction) # Patrol
    #visited_positions = grid.get_unique_visited_positions()
    print("Original path count: ", len(grid.get_unique_visited_positions()))
    #exit()
    # Hack add obstacle
    #grid.add_obstacle((7, 7))

    #print("Visited positions: ", grid.visited_positions)
    print("Starting loop detection for full path...")
    loop_count = 0
    round = 0
    total_positions = len(grid.visited_positions)
    visited_positions = grid.visited_positions
    obstacle_positions = []
    #for row, col in visited_positions:
    for i in range(0, len(visited_positions)):
        row = visited_positions[i][0][0]
        col = visited_positions[i][0][1]
        round += 1
        print("Round:", round, "/", total_positions, end=" ")
        grid = Grid(create_grid(input)) # Create a new grid
        if i == 0: # At first iteration, use the starting position
            position = grid.find_starting_position()
            direction = "up" # Set direction
            previously_visited_positions = []
        else: # At subsequent iterations, use the previous position and direction
            position = visited_positions[i-1][0]
            direction = visited_positions[i-1][1]
            previously_visited_positions = visited_positions[:i]
        grid.paint_position(position, direction) # Paint starting position
        if (row, col) == initial_position: # Skip starting position
            continue
        # Skip the positions that are on the previous path
        #print("Checking position: ", row, col)
        #print ("Visited positions: ", previously_visited_positions)
        previously_visited_places = [position for position, _ in previously_visited_positions]
        if (row, col) in previously_visited_places:
            #print ("Skipping position: ", row, col)
            continue

        grid.add_obstacle((row, col)) # Add obstacle
        print("Obstacle at: ", row, col, end=" ")
        pathpoints = patrol(grid, position, direction) # Patrol
        if pathpoints == 0:
            loop_count += 1
            print("Loop detected. Loop count: ", loop_count, end="\r")
            obstacle_positions.append((row, col))
            #grid.print()
    
    #print("Final loop count: ", loop_count)
    # Unique obstacle positions
    unique_obstacle_positions = list(set(obstacle_positions))
    print("Unique obstacle positions: ", unique_obstacle_positions)
    print("Unique obstacle positions: ", len(unique_obstacle_positions))


def main():
    starttime = time.time()
    #part1(get_input())
    #part1(test_input)
    part2(get_input())
    #part2(test_input5)
    endtime = time.time()
    print("Execution time: ", endtime-starttime)

    # Part2. 1902 is too low
    # Part2. 1903 is too low

    # Part2. 1986 in not correct
    # Part2. 2041 is not right
    # Part2. 2040 ???

    # Part2. 2125 is too high

if __name__ == "__main__":
    main()


