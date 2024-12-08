test_data = """
..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
.........."""

test_data2 = """
..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
.........."""

test_data3 = """
..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
.........."""

test_data4 = """
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#."""

test_data5 = """
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""


def get_input():
    with open("input.txt", "r") as file:
        return file.read()

def get_data(data):
    return [list(line) for line in data.split("\n") if line]


def find_antennas(data) -> dict:
    antennas = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char.isalpha() or char.isdigit():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
    return antennas


def find_antinodes_with_harmonics(antennas, data) -> set:
    ''' Antinodes are mirror images of antennas plus harmonics '''

    antinodes = {} # Antinodes are mirror images of antennas
    for antenna, coords in antennas.items():
        antinodes[antenna] = []
        for (i, j) in coords:
            for (x, y) in coords:
                # Skip the same antenna
                if i == x and j == y:
                    continue
                # Distance between antennas
                disx = x - i
                disy = y - j
                round = 1
                # This works for one round of harmonics
                #if 0 <= i-disx < len(data) and 0 <= j-disy < len(data[0]):
                #    antinodes[antenna].append((i-(x-i), j-(y-j)))
                while 0 <= i-disx*round < len(data) and 0 <= j-disy*round < len(data[0]):
                    antinodes[antenna].append((i-disx*round, j-disy*round))
                    round += 1
    return antinodes



def find_antinodes(antennas, data) -> set:
    ''' Antinodes are mirror images of antennas '''
    antinodes = {} # Antinodes are mirror images of antennas
    for antenna, coords in antennas.items():
        antinodes[antenna] = []
        for (i, j) in coords:
            for (x, y) in coords:
                # Skip the same antenna
                if i == x and j == y:
                    continue
                # Check if antinode fits the grid
                if 0 <= i-(x-i) < len(data) and 0 <= j-(y-j) < len(data[0]):
                    antinodes[antenna].append((i-(x-i), j-(y-j)))
    return antinodes


def get_unique_antinodes(antinodes):
    unique_antinodes = set()
    for antinode in antinodes.values():
        for node in antinode:
            unique_antinodes.add(node)
    return unique_antinodes


def print_grid(data, unique_antinodes=None):
    if unique_antinodes:
        for i, line in enumerate(data):
            for j, char in enumerate(line):
                if (i, j) in unique_antinodes:
                    print("*", end="")
                else:
                    print(char, end="")
            print()
    else:
        for line in data:
            print("".join(line))


def get_amount_of_antenna_harmonics(antennas, unique_antinodes):
    '''
    Calculate the amount of antennas when there is more than one antenna
    Exclude the single antennas
    Exclude antennas that are on the same location that any of the unique antinodes
    '''
    antenna_harmonics = 0
    for _, coords in antennas.items():
        if len(coords) > 1:
            for coord in coords:
                if coord in unique_antinodes:
                    continue
                antenna_harmonics += 1
    return antenna_harmonics


def part1(data):
    # Find antennas represented by alphabet or number characters on the grid
    antennas = find_antennas(data)
    #print(antennas)
    antinodes = find_antinodes(antennas, data)
    unique_antinodes = get_unique_antinodes(antinodes)
    print(unique_antinodes)
    return len(unique_antinodes)


def part2(data):
    # Find antennas represented by alphabet or number characters on the grid
    antennas = find_antennas(data)
    #print(antennas)
    antinodes = find_antinodes_with_harmonics(antennas, data)
    unique_antinodes = get_unique_antinodes(antinodes)
    print_grid(data, unique_antinodes)

    # Calculate number of antennas excluding the single antennas 
    # and antennas that are on the same location as any of the unique antinodes
    antenna_harmonics = get_amount_of_antenna_harmonics(antennas, unique_antinodes)
    #print(f"Antenna harmonics: {antenna_harmonics}")
    return len(unique_antinodes)+antenna_harmonics


def main():
    assert part1(get_data(test_data)) == 2
    assert part1(get_data(test_data2)) == 4
    assert part1(get_data(test_data3)) == 4
    assert part1(get_data(test_data4)) == 14

    data = get_data(get_input())
    #data = get_data(test_data5)
    #print_grid(data)

    #print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()