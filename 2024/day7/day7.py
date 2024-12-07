import itertools

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def parse_input(input):
    input = input.split("\n")
    for i, line in enumerate(input):
        input[i] = line.split(": ")
        input[i][0] = int(input[i][0])
        input[i][1] = input[i][1].split(" ")
        for j, num in enumerate(input[i][1]):
            input[i][1][j] = int(num)
            
    return input


def get_combinations(input, operators):
    ''' Get all possible combinations of operations '''
    numbers = input[1]
    operations_length = len(numbers)-1 # Number of operations to be performed (one less than the number of numbers)
    combinations = list(itertools.product(operators, repeat=operations_length))
    return combinations


def calculate_equation(equation, combination):
    ''' Calculate the equation '''
    numbers = equation[1]
    result = numbers[0]
    for i, num in enumerate(numbers[1:]):
        if combination[i] == "+":
            result += num
        elif combination[i] == "*":
            result *= num
        elif combination[i] == "&":
            result = int(str(result)+str(num))
            print(result)
    if result == equation[0]:
        print(f"Equation: {equation} = {result}, with combination: {combination}")
        return True
    return False


def part1(input):
    operators = ["+", "*"]
    parsed_input = parse_input(input)
    sum_of_valid_equations = 0
    for equation in parsed_input:
        operator_combinations = get_combinations(equation, operators)
        for combination in operator_combinations:
            if calculate_equation(equation, combination):
                sum_of_valid_equations += equation[0]
                break
    print(f"Sum of valid equations: {sum_of_valid_equations}")


def part2(input):
    operators = ["+", "*", "&"]
    parsed_input = parse_input(input)
    sum_of_valid_equations = 0
    for equation in parsed_input:
        operator_combinations = get_combinations(equation, operators)
        #print(operator_combinations)
        for combination in operator_combinations:
            if calculate_equation(equation, combination):
                sum_of_valid_equations += equation[0]
                break
    print(f"Sum of valid equations: {sum_of_valid_equations}")


def main():

    assert get_combinations([10, [1, 2, 3]], ["+", "*"]) == [('+', '+'), ('+', '*'), ('*', '+'), ('*', '*')]
    assert get_combinations([10, [1, 2, 3]], ["+", "*", "&"]) == [('+', '+'), ('+', '*'), ('+', '&'), ('*', '+'), ('*', '*'), ('*', '&'), ('&', '+'), ('&', '*'), ('&', '&')]
    assert calculate_equation([10, [1, 2, 3]], ('+', '+')) is False
    assert calculate_equation([9, [1, 2, 3]], ('+', '*')) is True
    assert calculate_equation([12, [1, 2]], ('&')) is True

    #part1(get_input())
    #part1(test_input)
    part2(get_input())
    #part2(test_input)


if __name__ == "__main__":
    main()