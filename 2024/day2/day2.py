# Advent of code 2024: Day 2
# https://adventofcode.com/2024/day/2

# Get the input data
with open('input.txt') as f:
    data = f.readlines()

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
def check_report_up(report):
    for i in range(1, len(report)):
        if report[i] - report[i - 1] >= 1 and report[i] - report[i - 1]  <= 3:
            continue
        else:
            print (f"Report is not safe: {report} because of {report[i]} and {report[i - 1]}")
        

def check_report_down(report):
    for i in range(1, len(report)):
        if report[i] - report[i - 1] <= -1 and report[i] - report[i - 1] >= -3:
            continue
        else:
            print (f"Report is not safe: {report} because of {report[i]} and {report[i - 1]}")


def check_report_orientation(report):
    if report[0] < report[-1]:
        check_report_up(report)
    else:
        check_report_down(report)

def check_report(report):
    check_report_up(report)
    check_report_down(report)


# Part 2 - Reports with dampener
def part2(data):
    # Split the data into a list of strings
    data = data.split('\n')
    for report in data:
        # Split the report into a list of numbers
        report = report.split(' ')
        # Convert the list of strings to a list of integers
        report = list(map(int, report))
        check_report(report)


def main():
    part2(testdata)


if __name__ == '__main__':
    main()
