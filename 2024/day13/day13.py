test_data1 = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def get_input_data(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()
    

def get_test_data(data):
    data = data.strip().split("\n")
    matrix = []
    for line in data:
        line = line.split("\n")
        matrix.append(line)
    return matrix


def solve_equation_pair(equation1, equation2):
    """
    Solve equation pair
    a1x + b1y = c1
    a2x + b2y = c2
    """

    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    # Calculate determinant
    det = a1*b2 - a2*b1

    # Calculate x
    x = (c1*b2 - c2*b1) / det

    # Calculate y
    y = (a1*c2 - a2*c1) / det

    return x, y


def handle_cost(x, y):
    """ Handle cost """
    if x > 100 or y > 100: # No prize
        return 0
    
    if x == round(x) and y == round(y):
        return int(x)*3 + int(y)
    
    return 0


def part1(data):

    assert 80.0, 40.0 == solve_equation_pair((94, 22, 8400), (34, 67, 5400))
    assert 38.0, 86.0 == solve_equation_pair((17, 84, 7870), (86, 37, 6450))
    assert 141.40454076367388, 135.3952528379773 == solve_equation_pair((26, 67, 12748), (66, 21, 12176))
    x, y = solve_equation_pair((26, 67, 10000000012748), (66, 21, 10000000012176))
    print(x, y)
    

    # Scan data
    cost = 0
    for row in data:
        print(row)
        if row[0].startswith("Button A"):
            # Get button A coordinates
            x_y = row[0].split(":")[1].strip()
            x, y = x_y.split(",")
            x1 = int(x.split("+")[1])
            y2 = int(y.split("+")[1])
        if row[0].startswith("Button B"):
            # Get button B coordinates
            x_y = row[0].split(":")[1].strip()
            x, y = x_y.split(",")
            x2 = int(x.split("+")[1])
            y3 = int(y.split("+")[1])
        if row[0].startswith("Prize"):
            # Get prize coordinates
            c_c = row[0].split(":")[1].strip()
            c1, c2 = c_c.split(",")
            c1 = int(c1.split("=")[1])
            c2 = int(c2.split("=")[1])

            # Solve equation pair
            x, y = solve_equation_pair((x1, x2, c1), (y2, y3, c2))
            cost += handle_cost(x, y)
            print(x, y)
    print(cost)


def main():
    #data = get_test_data(test_data1)
    data = get_test_data(get_input_data("input.txt"))
    part1(data)


if __name__ == "__main__":
    main()


#Tests

def solve_equation1_test():
    assert solve_equation_pair((94, 22, 8400), (34, 67, 5400)) == (8400, 5400)
    assert solve_equation_pair((17, 84, 7870), (86, 37, 6450)) == (7870, 6450)
    assert solve_equation_pair((69, 27, 18641), (23, 71, 10279)) == (18641, 10279)