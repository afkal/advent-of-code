import concurrent.futures
import time

test_data = "125 17"

input_data = "8069 87014 98 809367 525 0 9494914 5"


def get_input_data(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read().strip()
    return data

class LinkedList:

    def __init__(self):
        self.head = None
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next
            return node

    def add(self, value):
        """ Add a node to the end of linked list """
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def insert(self, node, value):
        """ Insert a node after a given node """
        new_node = Node(value, node.next)
        #new_node.next = node.next
        node.next = new_node
        #return new_node


    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        current = self.head
        print("{", end="")
        while current is not None:
            print(current.value, end=".")
            current = current.next
        print("}")
        return ""

class Node:

    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)
       

def get_input(input):
    input = input.split(" ")
    input = [int(i) for i in input]
    return input


def has_even_digits(stone):
    stone_str = str(stone)
    return len(stone_str) % 2 == 0


def modify_stone(stone):
    # If the stone is engraved with the number 0,
    # it is replaced by a stone engraved with the number 1.
    if stone == 0:
        return (1)
    # If the stone is engraved with an even number of digits,
    # it is replaced by two stones, each engraved with half of the digits
    # of the original stone.
    if has_even_digits(stone):
        stone_str = str(stone)
        midpoint = len(str(stone_str)) // 2
        stone1 = stone_str[:midpoint]
        stone2 = stone_str[midpoint:]
        return (int(stone1), int(stone2))
    # If none of the other rules apply, the stone is multiplied by 2024
    return (stone * 2024)


def store_ll_to_file(ll):
    with open("output.txt", "w") as file:
        current = ll.head
        while current:
            file.write(str(current.value) + " ")
            current = current.next


def part1(input):

    # Loop through input list 25 times
    for i in range(75):
        print("Iteration: ", i)
        output = []
        for item in input:
            # Create a linked list item
            #ll.add(Node(item))
            # Get modified stone
            item = modify_stone(item)
            if isinstance(item, tuple):
                output.append(item[0])
                output.append(item[1])
            else:
                output.append(item)
        input = output

    return len(output)


def process_node(node):
    item = modify_stone(node.value)
    if isinstance(item, tuple):
        return (node, item[0], item[1])
    else:
        return (node, item)
    

def change_stones_concurrent(input, blinks):
    """ Concurrently loop through input list 75 times """
    ll = LinkedList()
    for item in input:
        ll.add(item)

    for i in range(blinks):
        #print("Iteration:", i+1, end=" ")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(process_node, node): node for node in ll}
            for future in concurrent.futures.as_completed(futures):
                node, *values = future.result()
                #print("Node: ", node, "Values: ", values)
                if len(values) == 2:
                    node.value = values[0]
                    new_node = ll.insert(node, values[1])
                else:
                    node.value = values[0]
        #print(ll. size())
    return ll.size()


def change_stones2(input, blinks):

    for _ in range(blinks):
        #print("Iteration: ", i+1)
        output = []
        for item in input:
            item = modify_stone(item)
            if isinstance(item, tuple):
                output.append(item[0])
                output.append(item[1])
            else:
                output.append(item)
        input = output
    return output


def process_item(item):
    modified_item = modify_stone(item)
    if isinstance(modified_item, tuple):
        return [modified_item[0], modified_item[1]]
    else:
        return [modified_item]
    

def change_stones3(input, blinks):
    """ Change stones2 with concurrent processing """
    for _ in range(blinks):
        #print("Iteration: ", i+1)
        output = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_item, item) for item in input]
            for future in concurrent.futures.as_completed(futures):
                output.extend(future.result())
        input = output
    return output
  

def change_stones(input, blinks):

    # Populate linked list
    ll = LinkedList()
    for item in input:
        ll.add(item)

    for i in range(blinks):
        start = time.perf_counter()
        #print("Iteration: ", i+1)
        current = ll.head
        while current:
            #print("Node: ", current, "->", end=" ")
            # Get modified stone
            modify_stone_start = time.perf_counter()
            item = modify_stone(current.value)
            modify_stone_end = time.perf_counter()
            if modify_stone_end-modify_stone_start>1:
                print("Mod stone time: ", modify_stone_end-modify_stone_start)
            #print("Item: ", item)
            # Add modified stone to output list
            if_item = time.perf_counter()
            if isinstance(item, tuple):
                current.value = item[0]
                current_next = current.next
                #print("current: ", current, current.next)
                start_insert = time.perf_counter()
                ll.insert(current, item[1])
                end_insert = time.perf_counter()
                if end_insert-start_insert>1:
                    print("Insert time: ", end_insert-start_insert)
                current = current_next
            else:
                current.value = item
                current = current.next
            if_end = time.perf_counter()
            if if_end-if_item>1:
                print("If time: ", if_end-if_item)
        end = time.perf_counter()
        if end-start>1:
            print("Loop time: ", end-start)
        #print("Size: ", ll.size())
    return ll

# Part 2 Pro version results:
# Iteration:  41
# If time:  42.38169574999995
# If time:  69.80419849999998
# Loop time:  247.59506291600002

# Iteration:  40
# Insert time:  7.442919624999973
# If time:  7.442966041000005
# Loop time:  95.952369
# Size:  96753123

# Iteration:  41
# Insert time:  10.435125958000015
# If time:  10.435181958999976
# Insert time:  71.79476087500001
# If time:  71.794957958
# Loop time:  224.634083208

# Iteration:  40
# Insert time:  7.249444791000002
# If time:  7.24951304199999
# Loop time:  93.64990683299999

# Uusi tapa ilman linked listiä
# Iteration:  41
# Time:  53.617411917
# 44059301
# Iteration:  41
# Total changes:  44059301
# Time:  55.145300375000005
# 44059301




def change_stones_old(input):
    """ Loop through input list 75 times using linked list """

    # Populate linked list
    ll = LinkedList()
    for item in input:
        ll.add(item)
    
    for i in range(75):
        print("Iteration: ", i+1)
        for node in ll:
            # Get modified stone
            item = modify_stone(node.value)
            # Add modified stone to output list
            if isinstance(item, tuple):
                node.value = item[0]
                ll.insert(node, item[1])
            else:
                node.value = item

    return ll.size()


def calculate_total_stones(stones):
    total = 0
    for _, value in stones.items():
        total += value
    return total


def change_stones_dict(input, blinks):
    """ Loop through input list using dictionary """

    # Populate dictionary with stones as keys and number of stones as values
    stones_input = {}
    for item in input:
        stones_input[item] = stones_input.get(item, 0) + 1

    for i in range(blinks):
        print("Iteration: ", i+1)
        stones_output = {}
        for key, value in stones_input.items():
            # Get modified stone
            item = modify_stone(key)
            # Add modified stone to output list
            if isinstance(item, tuple):
                stones_output[item[0]] = stones_output.get(item[0], 0) + value
                stones_output[item[1]] = stones_output.get(item[1], 0) + value
            else:
                stones_output[item] = stones_output.get(item, 0) + value
        stones_input = stones_output
    print("Stones: ", stones_output)

    return calculate_total_stones(stones_output)

def linked_list_to_list(ll):
    output = []
    for node in ll:
        output.append(node.value)
    return output


def part2(input):
    start = time.perf_counter()

    #Change stones 75 times with 3 times 25 blinks one stone at a time
    total_stones = 0
    # for i, stone in enumerate(input):
    #     #print("Stone: ", i+1, "/", len(input))
    #     stones25 = change_stones_dict([stone], 25)
    #     #for j, stone in enumerate(linked_list_to_list(stones25)):
    #     for j, stone in enumerate(stones25):
    #         stones50 = change_stones2([stone], 25)
    #         #total_stones += len(stones50)
    #         print("Stone: ", i+1, "/", len(input),", ", j+1, "/", len(stones25), "Total stones: ", total_stones, "                    ")
    #         for _, stone in enumerate(stones50):
    #             stones75 = change_stones2([stone], 25)
    #             total_stones += len(stones75)
                #print("Stone: ", i+1, "/", len(input), j+1, "/", len(stones25), k+1, "/", len(stones50), "Total stones: ", total_stones, "                    ")

    total_stones = change_stones_dict(input, 75)

    end = time.perf_counter()
    print("Total changes: ", total_stones)
    print("Time: ", end-start)
    return total_stones



def main():
    print("Day 11")
    input = get_input(input_data)
    #input = get_input(get_input_data("output.txt"))
    #print(input)
    result = part2(input)
    print(result)

    # Part 2 test results:
    #[125 17] -> 55312 (Round 25)
    #[125 17] -> 445882 (Round 30)
    #[125 17] -> 29115525 (Round 40)
    #[125 17] -> 65601038650482 (Round 75)
                #65601038650482

    # Part 2 Pro version results:
    # Round 40: 96753123
    # "Actual answer is 15 digits long"


if __name__ == "__main__":
    main()