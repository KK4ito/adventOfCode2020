# with open('testInput.txt', 'r') as f:
# with open('part2_testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def construct_dict_from_inp(inp):
    root_bag = {}
    for strInput in inp:
        spl_str = strInput.split(" contain ")
        parent = spl_str[0].replace("bags", "").replace("bag", "").strip()
        child_elements = spl_str[1].replace(".", "").split(", ")
        parent_bag = {}
        for child_ele in child_elements:
            number = child_ele[0]
            if number != "n":
                child_bag = child_ele[2:].replace("bags", "").replace("bag", "").strip()
                parent_bag[child_bag] = int(number)
        root_bag[parent] = parent_bag
    return root_bag


def recursive_check_bag_for_parameter(root_bag, skip_bag, bag):
    cnt_shiny_bags = 0
    for entry in root_bag:
        if bag in root_bag[entry] and entry not in skip_bag:
            cnt_shiny_bags += 1
            skip_bag[entry] = 1
            cnt_shiny_bags += recursive_check_bag_for_parameter(root_bag, skip_bag, entry)
    return cnt_shiny_bags


def recursive_count_for_parameter(root_bag, bag):
    cnt_total = 0
    if bag in root_bag:
        cnt_total += sum(root_bag[bag].values())
        for entry_key, entry_value in root_bag[bag].items():
            cnt_total += entry_value * recursive_count_for_parameter(root_bag, entry_key)
    return cnt_total


def part1(inp, bag):
    root_bag = construct_dict_from_inp(inp)
    cnt_shiny_bags = recursive_check_bag_for_parameter(root_bag, {}, bag)
    print(cnt_shiny_bags)


def part2(inp, bag):
    root_bag = construct_dict_from_inp(inp)
    cnt_total = recursive_count_for_parameter(root_bag, bag)
    print(cnt_total)


part1(puzzleInput, "shiny gold")
part2(puzzleInput, "shiny gold")
