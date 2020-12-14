import itertools

# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def part1(inp):
    memory_dict = {}
    for line in inp:
        if line.startswith("mask = "):
            bitmask = line.replace("mask = ", "")
        elif line.startswith("mem"):
            line_splitted = line.split(" = ")
            memory_index = int((line_splitted[0])[4:-1])
            decimal_to_save = int(line_splitted[1])
            decimal_to_save_binary = format(decimal_to_save, '036b')
            result = []
            for idx, char in enumerate(bitmask):
                if char == 'X':
                    result.append(decimal_to_save_binary[idx])
                else:
                    result.append(char)
            memory_dict[memory_index] = int(''.join(result), 2)
    return sum(memory_dict.values())


def part2(inp):
    memory_dict = {}
    for line in inp:
        if line.startswith("mask = "):
            bitmask = line.replace("mask = ", "")
        elif line.startswith("mem"):
            line_splitted = line.split(" = ")
            memory_index = int((line_splitted[0])[4:-1])
            memory_index_binary = format(memory_index, '036b')
            decimal_to_save = int(line_splitted[1])
            memory_address_with_floating_value = []
            floating_cnt = 0
            floating_idx = []
            for idx, char in enumerate(bitmask):
                if char == '0':
                    memory_address_with_floating_value.append(memory_index_binary[idx])
                elif char == '1':
                    memory_address_with_floating_value.append('1')
                else:
                    floating_cnt += 1
                    floating_idx.append(idx)
                    memory_address_with_floating_value.append('X')

            # get all possible memory values
            floating_list_value = [list(i) for i in itertools.product([0, 1], repeat=floating_cnt)]
            for floating_list_value_entry in floating_list_value:
                for idx, floating_bit in enumerate(floating_list_value_entry):
                    memory_address_with_floating_value[floating_idx[idx]] = str(floating_bit)
                memory_dict[int(''.join(memory_address_with_floating_value), 2)] = decimal_to_save
    return sum(memory_dict.values())


print(part1(puzzleInput))
print(part2(puzzleInput))
