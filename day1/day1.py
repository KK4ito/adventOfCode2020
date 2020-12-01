import time

with open('part1.txt', 'r') as f:
    puzzleInput = [int(x.strip()) for x in f]


def part1(target, inp):
    for x in inp:
        if target - x in inp:
            return x, target - x


def part2(target, inp):
    for x in inp:
        for y in inp:
            if target - x - y in inp:
                return x, y, target - x - y


# Part 1
part1TimeStart = time.time()
solution = part1(2020, puzzleInput)
part1TimeEnd = time.time()
print(solution[0] * solution[1])
print("elapsed time: " + str(part1TimeEnd - part1TimeStart))

# Part 2
part2TimeStart = time.time()
solution_part2 = part2(2020, puzzleInput)
part2TimeEnd = time.time()
print(solution_part2[0] * solution_part2[1] * solution_part2[2])
print("elapsed time: " + str(part2TimeEnd - part2TimeStart))
