

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""



def get_input():
    with open('input.txt') as f:
        input = f.read()
    return input


def parse_input(input):
    lines = input.split("\n")
    lines = [x.strip() for x in lines]
    ordering_rules = []
    pages = []
    for line in lines:
        if line == "":
            continue
        if "|" in line:
            ordering_rules.append(line.split("|"))
        else:
            pages.append(line.split(","))
    return (ordering_rules, pages)


def first_item_is_before_second(rule, list):
    first = rule[0]
    second = rule[1]
    if first not in list or second not in list:
        return True # If the items are not in the list, the rule is satisfied
    first_index = list.index(first)
    second_index = list.index(second)
    return first_index < second_index


def check_update_for_rules(update, rules):
    for rule in rules:
        if first_item_is_before_second(rule, update):
            # Rule is satisfied
            continue
        else:
            # Rule is not satisfied
            return False
    return True


def get_middle_page_number(update):
    """ Returns the midlle item of the list """
    return int(update[len(update) // 2])


def get_failing_updates(updates, rules):
    failing_updates = []
    for update in updates:
        if not check_update_for_rules(update, rules):
            failing_updates.append(update)
    return failing_updates


def sum_of_middle_page_numbers(updates):
    sum = 0
    for update in updates:
        sum += get_middle_page_number(update)
    return sum


def check_list_of_updates_against_rules(updates, rules):
    # Iterate over all the updates and check if all the rules are satisfied
    # If the rules are satisfied, add the middle page number to the sum and the list of failing updates
    succeeding_updates = []
    failing_updates = []
    for update in updates:
        if check_update_for_rules(update, rules):
            succeeding_updates.append(update)
        else:
            failing_updates.append(update)
    return succeeding_updates, failing_updates


def part1(input):
    ordering_rules, updates = parse_input(input)
    success, _ = check_list_of_updates_against_rules(updates, ordering_rules)
    return sum_of_middle_page_numbers(success)


def order_update(update, rules):
    """ Order the update based on the rules """
    while not check_update_for_rules(update, rules): # Loop while update is not ordered
        for rule in rules:
            if rule[0] not in update:
                continue
            if rule[1] not in update:
                continue
            if not first_item_is_before_second(rule, update):
                # If first item is after second item, move the second item right after the first item
                first_index = update.index(rule[0])
                second_index = update.index(rule[1])
                second_item = update.pop(second_index)
                update.insert(first_index, second_item)
    return update


def order_updates(updates, rules):
    """ Order the updates based on the rules """
    ordered_updates = []
    for update in updates:
        ordered_updates.append(order_update(update, rules))
    return ordered_updates


def part2(input):
    # Original input
    ordering_rules, updates = parse_input(input)
    # Get the succesfull and failing updates
    success, fail = check_list_of_updates_against_rules(updates, ordering_rules)
    print("Count of originally failing updates: " + str(len(fail)))
    updates = order_updates(fail, ordering_rules)
    success, fail = check_list_of_updates_against_rules(fail, ordering_rules)
    print("Count of failing updates after ordering: " + str(len(fail)))
    #print(success)
    return sum_of_middle_page_numbers(success)


def main():
    input = get_input()
    result = part1(input)
    #print(result)

    result = part2(input)
    print("Sum of middle page numbers: " + str(result))


if __name__ == "__main__":
    # Test cases
    assert first_item_is_before_second(["a", "c"], ["a", "b", "c", "d"]) == True
    assert first_item_is_before_second(["c", "b"], ["a", "b", "c", "d"]) != True
    main()