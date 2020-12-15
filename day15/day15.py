# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def memory_with_round(inp, max_round):
    list_numbers = inp[0].split(',')
    previous = {int(x): i + 1 for i, x in enumerate(list_numbers)}
    last = list_numbers[-1]
    for r in range(len(list_numbers) + 1, max_round + 1):
        current = r - 1 - previous[last] if last in previous else 0
        previous[last] = r - 1
        last = current

    return last


def part1(inp, max_round):
    return memory_with_round(inp, max_round)


def part2(inp, max_round):
    return memory_with_round(inp, max_round)


print(part1(puzzleInput, 2020))
print(part2(puzzleInput, 30000000))
