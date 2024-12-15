

test_input1 = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def get_input(file):
    data = ""
    with open(file, "r") as file:
        data = file.read().strip()
    return data


def get_data(data):
    data = data.strip().split("\n")
    data_table = []
    for row in data:
        row = row.split(" ")
        point = row[0].split("=")[1].split(",")
        velocity = row[1].split("=")[1].split(",")
        data_table.append((point, velocity))
    return data_table


def move_robot(point, velocity):
    """ Move robot one step """
    x = int(point[0]) + int(velocity[0])
    y = int(point[1]) + int(velocity[1])
    return (x, y)


def move_robots(input):
    """ Move robots one step """
    output = []
    for row in input:
        point = row[0]
        velocity = row[1]
        point = move_robot(point, velocity)
        output.append((point, velocity))
    return output


def handle_teleports(input, width, height):
    """ Handle teleports """
    output = []
    for row in input:
        x = row[0][0]
        y = row[0][1]
        if x < 0 or x >= width:
            x = x % width
        if y < 0 or y >= height:
            y = y % height
        #print("Teleporting to: ", x, y)
        output.append(([x,y], row[1]))
    return output


def print_data(data_table, width, height):
    for i in range(height):
        for j in range(width):
            # Check if point is in data_table
            point = [j, i]
            found = False
            for row in data_table:
                if point == row[0]:
                    found = True
                    break
            if found:
                print("o", end="")
            else:
                print(".", end="")
        print()


def count_points_per_quadrant(data_table, width, height):
    """ Count number of data points per each quadrant """
    quadrants = {}
    width = width-1
    height = height-1
    for row in data_table:
        x = row[0][0]
        y = row[0][1]
        if x < width/2 and y < height/2:
            if "1" in quadrants:
                quadrants["1"] += 1
            else:
                quadrants["1"] = 1
        elif x > width/2 and y < height/2:
            if "2" in quadrants:
                quadrants["2"] += 1
            else:
                quadrants["2"] = 1
        elif x < width/2 and y > height/2:
            if "3" in quadrants:
                quadrants["3"] += 1
            else:
                quadrants["3"] = 1
        elif x > width/2 and y > height/2:
            if "4" in quadrants:
                quadrants["4"] += 1
            else:
                quadrants["4"] = 1
    return quadrants


def count_safety_factor(quadrants):
    """ Calculate safety factor by multiplying all values in quadrants """
    result = 1
    for key, value in quadrants.items():
        result *= value
    return result


def check_easter_egg(data_table):
    """ Check if easter egg is found """
    #print("Checking for easter egg")
    #print(data_table)
    points = []
    for row in data_table:
        points.append((row[0][0], row[0][1]))
    #print(points)
    # Check if there is a square of 9 points
    for i, (x, y) in enumerate(points):
        if (x+1, y) in points and (x+2, y) in points:
            if (x, y+1) in points and (x+1, y+1) in points and (x+2, y+1) in points:
                if (x, y+2) in points and (x+1, y+2) in points and (x+2, y+2) in points:
                    print("Easter egg found")
                    return True
    return False

def part1(data_table, width, height):

    for i in range(100000):
        print("Step: ", i+1, end="\r")
        data_table = move_robots(data_table)
        data_table = handle_teleports(data_table, width, height)
        if check_easter_egg(data_table):
            print("Easter egg found at step: ", i+1)
            print_data(data_table, width, height)
            print()
            break

    data_table = handle_teleports(data_table, width, height)
    #print_data(data_table, width, height)
    quadrants=count_points_per_quadrant(data_table, width, height)
    return count_safety_factor(quadrants)


def main():
    width = 101
    height = 103
    input = get_input("input.txt")

    #width = 11
    #height = 7
    #input = test_input1

    data_table = get_data(input)
    result = part1(data_table, width, height)
    print(result)


if __name__ == "__main__":
    main()