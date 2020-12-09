from itertools import combinations

# with open('testInput.txt', 'r') as f:
# with open('part2_testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [int(x.strip()) for x in f]


def find_pairs(list_numbers, sum_to_find):
    return find_combo_with_n(list_numbers, sum_to_find, 2)


def find_combo_with_n(list_numbers, sum_to_find, n):
    return [pair for pair in combinations(list_numbers, n) if sum(pair) == sum_to_find]


def part1(inp, preamble):
    index = 0
    sum_to_test = inp[preamble:]

    for number in sum_to_test:
        list_numbers = inp[index:preamble + index]
        index += 1
        if not find_pairs(list_numbers, number):
            return number
    return None


def part2(inp, to_find_sum):
    x, y = 0, 0
    while sum(inp[x:x + y + 2]) != to_find_sum:
        if sum(inp[x:x + y + 2]) <= to_find_sum:
            y += 1
        else:
            x += 1
            y = 0

    return max(inp[x:x + y + 2]) + min(inp[x:x + y + 2])


invalid_number = part1(puzzleInput, 25)
print(invalid_number)
print(part2(puzzleInput, invalid_number))
