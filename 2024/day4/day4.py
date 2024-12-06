

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def get_input():
    with open('input.txt') as f:
        lines = f.read()
    #lines = [x.strip() for x in lines]
    return lines



def create_char_matrix(input: str):
    lines = input.split("\n")
    char_matrix = []
    for line in lines:
        char_matrix.append([char for char in line])
    return char_matrix

def find_letter_coordinates(char_matrix, letter):
    coordinates = []
    for i in range(len(char_matrix)):
        for j in range(len(char_matrix[i])):
            if char_matrix[i][j] == letter:
                coordinates.append((i, j))
    return coordinates


def search_word(char_matrix, coordinates, word):
    """ Search for word in matrix """

    # Split word into list of characters
    word = list(word)
    
    matches = 0
    # Check if word is in matrix from coordinates left to right
    for i in range(len(word)):
        if coordinates[1] + i >= len(char_matrix[0]):
            break
        if char_matrix[coordinates[0]][coordinates[1] + i] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates right to left
    for i in range(len(word)):
        if coordinates[1] - i < 0:
            break
        if char_matrix[coordinates[0]][coordinates[1] - i] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates top to bottom
    for i in range(len(word)):
        if coordinates[0] + i >= len(char_matrix):
            break
        if char_matrix[coordinates[0] + i][coordinates[1]] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates bottom to top
    for i in range(len(word)):
        if coordinates[0] - i < 0:
            break
        if char_matrix[coordinates[0] - i][coordinates[1]] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates top left to bottom right
    for i in range(len(word)):
        if coordinates[0] + i >= len(char_matrix) or coordinates[1] + i >= len(char_matrix[0]):
            break
        if char_matrix[coordinates[0] + i][coordinates[1] + i] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates bottom right to top left
    for i in range(len(word)):
        if coordinates[0] - i < 0 or coordinates[1] - i < 0:
            break
        if char_matrix[coordinates[0] - i][coordinates[1] - i] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates top right to bottom left
    for i in range(len(word)):
        if coordinates[0] + i >= len(char_matrix) or coordinates[1] - i < 0:
            break
        if char_matrix[coordinates[0] + i][coordinates[1] - i] != word[i]:
            break
    else:
        matches += 1

    # Check if word is in matrix from coordinates bottom left to top right
    for i in range(len(word)):
        if coordinates[0] - i < 0 or coordinates[1] + i >= len(char_matrix[0]):
            break
        if char_matrix[coordinates[0] - i][coordinates[1] + i] != word[i]:
            break
    else:
        matches += 1

    return matches


def search_star(char_matrix, coordinates):
    """ Search for star in matrix """

    # Check if we are at the edge of the matrix
    if coordinates[0] + 1 >= len(char_matrix) or coordinates[1] + 1 >= len(char_matrix[0]):
        return 0
    
    if coordinates[0] - 1 < 0 or coordinates[1] - 1 < 0:
        return 0

    # Check if we have a star
    if char_matrix[coordinates[0] + 1][coordinates[1] + 1] == 'S' and char_matrix[coordinates[0] - 1][coordinates[1]-1] == 'M' or char_matrix[coordinates[0] + 1][coordinates[1] + 1] == 'M' and char_matrix[coordinates[0] - 1][coordinates[1]-1] == 'S':
        if char_matrix[coordinates[0] + 1][coordinates[1] - 1] == 'S' and char_matrix[coordinates[0] - 1][coordinates[1]+1] == 'M' or char_matrix[coordinates[0] + 1][coordinates[1] - 1] == 'M' and char_matrix[coordinates[0] - 1][coordinates[1]+1] == 'S':
            return 1
    
    return 0

def search_word_count(char_matrix, word, initial_coordinates):
    """ Return count of word in matrix """
    found = 0
    for cordinates in initial_coordinates:
        found += search_word(char_matrix, cordinates, word)
    return found


def search_word_stars(char_matrix, initial_coordinates):
    """ Return count of word stars in matrix """
    found = 0
    for cordinates in initial_coordinates:
        found += search_star(char_matrix, cordinates)
    return found


def part1(input: str):
    char_matrix = create_char_matrix(input)
    print(char_matrix)
    # Find coordinates of letter X as start for XMAS
    x_cords=find_letter_coordinates(char_matrix, 'X')
    print(search_word_count(char_matrix, "XMAS", x_cords))


def part2(input: str):
    char_matrix = create_char_matrix(input)
    print(char_matrix)
    # Find coordinates of letter A as a center for X-MAS
    a_cords=find_letter_coordinates(char_matrix, 'A')
    print(search_word_stars(char_matrix, a_cords))


def main():
    print("Day 4")
    input = get_input()
    #part1(input)
    part2(input)

if __name__ == '__main__':
    main()