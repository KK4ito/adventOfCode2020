# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def map_traverse(move_right, move_down, inp):
    right_end = len(inp[0])
    down_end = len(inp)
    start_x = 0
    start_y = 0
    cnt_trees_hit = 0

    while start_y < down_end:
        current = inp[start_y][start_x]
        if current == "#":
            cnt_trees_hit = cnt_trees_hit + 1
        start_x = start_x + move_right
        start_y = start_y + move_down
        if start_x >= right_end:
            start_x = start_x - right_end

    return cnt_trees_hit


def part1(inp):
    print(map_traverse(3, 1, inp))


def part2(inp):
    result = map_traverse(1, 1, inp) * map_traverse(3, 1, inp) \
             * map_traverse(5, 1, inp) * map_traverse(7, 1, inp) * map_traverse(1, 2, inp)
    print(result)


part1(puzzleInput)
part2(puzzleInput)
