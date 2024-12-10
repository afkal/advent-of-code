from collections import deque

test_data1 = "12345"
test_data2 = "2333133121414131402"


memory_vector = [] # part 2 data structure
file_queue = deque() # part 1 data structure
empty_slots = [] # part 1 data structure
files = [] # part 2 data structure

def get_input_data(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def add_file_queue(file_index, file_size):
    ''' Add file indexes to file_queue '''
    global file_queue
    for i in range(file_size):
        file_queue.append(file_index)


def add_to_memory_vector(memory_index, file_index, file_size, space_size):
    ''' Add new file and space to memory list '''
    global memory_vector

    # Loop from memory_index to file_size and add file_index to memory_vector
    for i in range(memory_index, memory_index+file_size):
        memory_vector.append(file_index)

    # Loop from file_size to space_size and add None to memory_vector
    if space_size is not None: # Handle end of disk map
        for i in range(memory_index+file_size, memory_index+file_size+space_size):
            memory_vector.append(None)


def populate_memory(data):
    memory_index = 0
    for i in range(0, len(data), 2):
        file_size = int(data[i])
        file_index = i//2

        # Part 1. Add files to file_queue
        add_file_queue(file_index, file_size)

        # Part 2. Add files to files dictionary
        file = (file_index, memory_index, file_size)
        files.append(file)

        if i+1 >= len(data): # End of disk map - skip final spaces
            add_to_memory_vector(memory_index, file_index, file_size, None)
            break
        space_size = int(data[i+1])
        
        # Part 1. and Part 2. Add empty slots to empty_slots list
        empty_slots.append((memory_index+file_size, space_size))

        add_to_memory_vector(memory_index, file_index, file_size, space_size)
        memory_index += file_size + space_size
        

def calculate_checksum(memory_vector):
    checksum = 0
    for i, value in enumerate(memory_vector):
        if value is None:
            continue
        #print(i, " * ", value, " = ", value * (i))
        checksum += value * (i)
    return checksum


def print_memory(memory_vector):
    for _, value in enumerate(memory_vector):
        if value is None:
            print(".", end="")
            continue
        print(value, end="")
    print()


def compact_memory(file_queue, empty_slots):
    ''' Compact memory by moving files to empty slots '''
    memory = []
    index = 0
    while file_queue:
        # Get next empty slot
        slot_start, slot_length = empty_slots.pop(0)
        #print("New empty slot_start: ", slot_start, " slot_length: ", slot_length)
        # Add files from the beginning until the empty slot
        while index < slot_start:
            #print("filling from the queue front: ", index, slot_start)
            if file_queue: # Check if queue is empty
                memory.append(file_queue.popleft())
            index += 1
        #print("memory: ", memory)
        # Add files from the end to the empty slot
        empty_slot_ends = index + slot_length
        while index < empty_slot_ends:
            #print("filling from the queue back: ", index, empty_slot_ends)
            if file_queue: # Check if queue is empty
                memory.append(file_queue.pop())
            index += 1
    return memory


def memory_vector_add(file_index, file_start, file_size):
    ''' Add file to memory '''
    global memory_vector
    for i in range(file_start, file_start+file_size):
        memory_vector.append(file_index)


def find_fitting_file(slot_length):
    ''' Find fitting file from the end '''
    for i in range(len(files)-1, -1, -1):
        _, _, file_size = files[i]
        if file_size <= slot_length:
            return files.pop(i)
    return None


def iterate_files():
    ''' Iterate over files and move them to empty slots starting from the end '''
    
    compact_mode = True # Compact mode feature flag
    while files:
        # Get next file
        file_index, file_start, file_size = files.pop(0)
        # Add file to memory_vector
        memory_vector_add(file_index, file_start, file_size)
        # Get next empty slot
        if not empty_slots: # Check if end of disk map
            continue
        slot_start, slot_length = empty_slots.pop(0)
        
        if compact_mode:
            # TODO: Scan files from the end and if file fits to empty slot, move it there
            # Scanning files from the end not yet implemented

            # TODO: Find fitting file from the end
            file = find_fitting_file(slot_length)
            if file is not None:
                file_index, slot_start, file_size = file
                # Add file to memory_vector
                memory_vector_add(file_index, slot_start, file_size)
                # Add empty slot to memory_vector
                memory_vector_add(None, slot_start+file_size, slot_length-file_size)
                #print_memory(memory_vector)
            else:
                # Add file to memory_vector
                memory_vector_add(file_index, slot_start, slot_length)
        else:
            # If no fitting file found add empty slot to memory_vector
            memory_vector_add(None, slot_start, slot_length)


def find_empty_slot_for_file(file_size):
    ''' Find empty slot for file from the beginning '''
    for i, slot in enumerate(empty_slots):
        _, slot_size = slot
        if slot_size >= file_size:
            return i
    return None


def move_file_to_empty_slot(file_index, file_start, file_size, slot_index):
    ''' Move file to empty slot in memory_vector '''
    global memory_vector
    slot_start, slot_size = empty_slots[slot_index]

    # Move only if empty slot is earlier in memory_vector than the original file
    if slot_start > file_start:
        return

    #print("moving file: ", file_index, " to slot: ", slot_index, " start: ", slot_start, " size: ", slot_size)
    for i in range(slot_start, slot_start+file_size):
        memory_vector[i] = file_index

    # Update empty slot
    empty_slots[slot_index] = (slot_start+file_size, slot_size-file_size)

    # Remove original file from memory_vector
    for i in range(file_start, file_start+file_size):
        memory_vector[i] = None # Simple way -> set to None

    # TODO: Add new empty slot to empty_slots list on the place of original file
    # Check if new empty slot is needed or if it can be merged with the previous ones


def compact_files():
    ''' Iterate over memory_vector and compact files to empty slots from the end '''
    global memory_vector
    compact_mode = True # Compact mode feature flag
    while files:
        # Get next file
        file_index, file_start, file_size = files.pop()
        print("=====================================")
        print("Processing file: ", file_index, file_start, file_size)
        print("=====================================")
        #  TODO: Check if file fits to empty slots from the beginning
        slot_index = find_empty_slot_for_file(file_size)
        if slot_index is not None:
            #print("file fits empty slot at index: ", slot_index)
            # Move file to empty slot
            move_file_to_empty_slot(file_index, file_start, file_size, slot_index)
        #print_memory(memory_vector)
        #print("files: ", files)
        #print("empty slots: ", empty_slots)


def part1(data):
    populate_memory(data)
    memory = compact_memory(file_queue, empty_slots)
    checksum = calculate_checksum(memory)
    return checksum


def part2(data):
    # Create initial memory_vector
    populate_memory(data)

    print("Initial conditions:")
    print ("Memory vector: ")
    print_memory(memory_vector)
    print ("Files: ", files)
    print ("Empty slots: ", empty_slots)
    print("-------------------")

    compact_files()
    #iterate_files()
    checksum = calculate_checksum(memory_vector)
    return checksum

    #6556224409884 -> too high
    #8553014718259 -> too high

def main():
    data = get_input_data("input.txt")

    ### Part 1 ###
    #print(part1(test_data2))
    #print(part1(data))

    ### Part 2 ###
    #print(part2(test_data2))
    print_memory(memory_vector)
    print(part2(data))



if __name__ == "__main__":
    main()


#00992111777.44.333....5555.6666.....8888..
#00992111777.44.333....5555.6666.....8888..

#empty slots:  [(4, 1), (8, 3), (12, 3), (18, 1), (21, 1), (26, 1), (31, 1), (35, 1), (40, 0)]
#empty slots:  [(4, 1), (8, 3), (12, 3), (18, 1), (21, 1), (26, 1), (31, 1), (35, 1), (40, 0)]
#empty slots:  [(4, 1), (11, 0), (12, 3), (18, 1), (21, 1), (26, 1), (31, 1), (35, 1), (40, 0)]