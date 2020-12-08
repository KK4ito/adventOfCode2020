# with open('testInput.txt', 'r') as f:
# with open('part2_testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def execute_line(index, dict_actions, accumulator, already_executed):
    if index in already_executed:
        return accumulator
    else:
        str_input = dict_actions[index]  # get first instruction

        already_executed.append(index)
        dict_actions[str_input] = 1
        split_line = str_input.split(" ")
        action = split_line[0]

        if action == "acc":
            number = int(split_line[1])
            accumulator += number
            index += 1
        elif action == "jmp":
            number = int(split_line[1])
            index += number
        else:  # nop action
            index += 1
        return execute_line(index, dict_actions, accumulator, already_executed)


def execute_line_swap(index, dict_actions, accumulator, already_executed):
    if index in already_executed:
        return None
    elif index == len(dict_actions):
        return accumulator
    else:
        str_input = dict_actions[index]  # get first instruction
        already_executed.append(index)
        split_line = str_input.split(" ")
        action = split_line[0]

        if action == "acc":
            number = int(split_line[1])
            accumulator += number
            index += 1
        elif action == "jmp":

            number = int(split_line[1])
            index += number
        else:  # nop action
            index += 1

        return execute_line_swap(index, dict_actions, accumulator, already_executed)


def part1(inp):
    accumulator = 0
    index = 0
    dict_actions = dict(enumerate(x for x in inp))
    already_executed = []

    total = execute_line(index, dict_actions, accumulator, already_executed)
    print(total)


def part2(inp):
    accumulator = 0
    index = 0
    dict_actions = dict(enumerate(x for x in inp))

    nop_or_jmp_dict = {key: dict_actions[key] for key in dict_actions.keys() if
                       str(dict_actions[key]).startswith("jmp") or str(dict_actions[key]).startswith("nop")}
    key_list = list(nop_or_jmp_dict.keys())
    total = None

    while total is None:
        dict_actions_copy = dict_actions.copy();
        command_to_swap = key_list[index]
        command = str(dict_actions_copy[command_to_swap])
        if command.startswith("nop"):
            dict_actions_copy[command_to_swap] = command.replace("nop", "jmp")
        elif command.startswith("jmp"):
            dict_actions_copy[command_to_swap] = command.replace("jmp", "nop")

        total = execute_line_swap(0, dict_actions_copy, accumulator, [])
        index += 1
    print(total)


part1(puzzleInput)
part2(puzzleInput)
