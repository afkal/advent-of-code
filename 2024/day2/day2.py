# Advent of code 2024: Day 2
# https://adventofcode.com/2024/day/2

# Get the input data
with open('input.txt') as f:
    data = f.read()

# test data
testdata = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


# Check if report is "safe"
#  * The levels are either all increasing or all decreasing
#  * Any two adjacent levels differ by at least one and at most three
#  * Reports tolerate a single bad item (when item is removed report should be safe)
def check_report_up(report) -> bool:
    for i in range(1, len(report)):
        if report[i] - report[i - 1] >= 1 and report[i] - report[i - 1]  <= 3:
            continue
        else:
            return False
    return True     

def check_report_down(report):
    for i in range(1, len(report)):
        if report[i] - report[i - 1] <= -1 and report[i] - report[i - 1] >= -3:
            continue
        else:
            return False
    return True

# Part 1.
def is_report_safe(report):
    return check_report_up(report) or check_report_down(report)


# Drop one item at the time from list to create new reports
def create_report_combinations(report):
    report_combinations = []
    for i in range(len(report)):
        report_combinations.append(report[:i] + report[i+1:])
    return report_combinations


# Part 2. Try to remove one item at the time from the report and check if it is safe
def is_report_safe2(report):
    report_combinations = create_report_combinations(report)
    for report in report_combinations:
        if is_report_safe(report):
            return True
    return False

# Part 1 - Normal report
def part1(data):
    # Split the data into a list of strings
    data = data.split('\n')

    count = 0
    for report in data:
        # Split the report into a list of numbers
        report = report.split(' ')
        # Convert the list of strings to a list of integers
        report = list(map(int, report))
        if is_report_safe(report):
            count += 1
    print(count)


def part2(data):
    # Split the data into a list of strings
    data = data.split('\n')

    count = 0
    for report in data:
        # Split the report into a list of numbers
        report = report.split(' ')
        # Convert the list of strings to a list of integers
        report = list(map(int, report))
        if is_report_safe2(report):
            count += 1
    print(count)


def main():
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
