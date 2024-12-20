from enum import Enum
instructions = {
    0: 'adv', # divide
    1: 'bxl', # bitwise XOR
    2: 'bst', # modulo
    3: 'jnz', # jump
    4: 'bxc', # bitwise XOR
    5: 'out', # output
    6: 'bdv', # divide
    7: 'cdv', # divide
}


class Instructions(Enum):
    ADV = 0 # divide
    BXL = 1 # bitwise XOR
    BST = 2 # modulo
    JNZ = 3 # jump
    BXC = 4 # bitwise XOR
    OUT = 5 # output
    BDV = 6 # divide B
    CDV = 7 # divide C


def get_combo(operand, registers):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers['A']
        case 5:
            return registers['B']
        case 6:
            return registers['C']
        case _:
            return "Invalid operand"


def run_program(registers, program):
    i = 0
    output = []
    while i < len(program):
        instr = int(program[i])
        operand = int(program[i+1])
        combo = get_combo(operand, registers)
        match instr:
            case Instructions.ADV.value: # divide A
                registers['A'] = int(registers['A'] / (2 ** combo))
                i += 2
            case Instructions.BXL.value: # bitwise XOR
                registers['B'] = registers['B'] ^ operand
                i += 2
            case Instructions.BST.value:
                registers['B'] = combo % 8
                i += 2
            case Instructions.JNZ.value:
                if registers['A'] != 0:
                    i = operand
                else:
                    i += 2
            case Instructions.BXC.value:
                registers['B'] = registers['B'] ^ registers['C']
                i += 2
            case Instructions.OUT.value:
                output.append(combo % 8)
                i += 2
            case Instructions.BDV.value:
                registers['B'] = int(registers['A'] / (2 ** combo))
                i += 2
            case Instructions.CDV.value:
                registers['C'] = int(registers['A'] / (2 ** combo))
                i += 2
            case _:
                print("Invalid instruction: ", instr)
                i += 2
    return (registers, output)


def part1():
    registers = {'A': 28066687, 'B': 0, 'C': 0}
    registers = {'A': 35184831900207, 'B': 0, 'C': 0}
    program = [2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0]
    registers, output=run_program(registers, program)
    print("Registers:", registers)
    print("Input: ",program)
    print("Output:",output)


def check_output_against_program(input, output, round):
    """ Check if the output matches the program """

    for i in range(len(output)):
        if output[0:7] == input[0:7]:
            print(f"Round {round} Output nearly matches program!!!")
            return 2

    if output == input:
        print(f"Round {round} Output matches program!!!")
        return 1
    return 0


def part2():

    close_to_matches = []
    matches = []
    program = [2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0]
    # Loop through all possible values of A register
    for i in range(35184833820000, 400000000000000):
        registers = {'A': i, 'B': 0, 'C': 0}
        registers,output=run_program(registers, program)
        # print("Registers:", registers)
        # print("Output:",output)
        # print("Program:", program)
        # print("Checking output")
        result = check_output_against_program(program, output, i)
        if result == 2:
            close_to_matches.append(i)
        if result == 1:
            matches.append(i)
            break
        if i % 10000 == 0:
            print("Round:", i, "len(output):", len(output), end="\r")


    print()
    print("Matches:", matches)
    print("Close to matches:", close_to_matches)

# 35184372016484
# 35184372000000 -> 16 output alkaa
#[5, 5, 5, 5, 2, 7, 5, 5, 5, 5, 5, 5, 5, 2, 2]
# 266666666666666
#[2, 5, 2, 5, 6, 5, 6, 7, 4, 0, 5, 3, 1, 6, 0, 2]
# 35184382633316
#[2, 4, 1, 1, 7, 5, 1, 0, 5, 5, 5, 5, 5, 5, 1, 5]
# 35184831900207
# 2, 4, 1, 1, 7, 5, 4, 0, 0, 6, 5, 5, 5, 5, 1, 5]


def test_instructions():
    registers = {'C': 9}
    program = [2,6]
    registers = run_program(registers, program)
    assert registers['B'] == 1

    registers = {'A': 10}
    program = [5,0,5,1,5,4]
    registers = run_program(registers, program)
    
    #TODO: Fix this test case
    registers = {'A': 2024}
    program = [0,1,5,4,3,0]
    registers = run_program(registers, program)
    #assert registers['A'] == 0 

    registers = {'B': 29}
    program = [1,7]
    registers = run_program(registers, program)
    assert registers['B'] == 26

    registers = {'B': 2024, 'C': 43690}
    program = [4,0]
    registers = run_program(registers, program)
    assert registers['B'] == 44354

    registers = {'A': 729, 'B': 0, 'C': 0}
    program = [0,1,5,4,3,0]
    registers=run_program(registers, program)
    assert registers['A'] == 0

    registers = {'A': 117440, 'B': 0, 'C': 0}
    program = [0,3,5,4,3,0]
    registers=run_program(registers, program)


def main():
    #test_instructions()
    part1()
    #part2()


if __name__ == "__main__":
    main()