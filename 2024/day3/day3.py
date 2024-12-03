# Get the input data
import re

input = ""
with open('input.txt') as f:
    input = f.read()


def filter_donts_untils_dos(data):
    new_data = ""
    enable = True
    #print(len(data))
    for i in range(len(data)):
        if data[i:i+7] == "don't()":
            enable = False
        if data[i:i+4] == "do()":
            enable = True
        if enable:
            new_data += data[i]
    return new_data


def find_multiplications(data):
    regexp = ("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    multiplications = re.findall(regexp, data)
    multiplications = [(int(a), int(b)) for a, b in multiplications]
    multiply = lambda x: x[0] * x[1]
    res = map(multiply, multiplications)

    total = 0
    for i in res:
        total += i
    print(total)

def main():
    testdata =   "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    filtered_input = filter_donts_untils_dos(input)
    find_multiplications(filtered_input)


if __name__ == '__main__':
    main()
