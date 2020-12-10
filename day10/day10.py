# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [int(x.strip()) for x in f]


def part1(inp):
    cnt_1 = 0
    cnt_3 = 1
    sorted_inp = sorted(inp)
    if sorted_inp[0] - 1 == 0:
        cnt_1 += 1
    else:
        cnt_3 += 1

    for curr_element in sorted_inp[:-1]:
        if curr_element + 1 in sorted_inp:
            cnt_1 += 1
        else:
            cnt_3 += 1

    print("1: " + str(cnt_1))
    print("3: " + str(cnt_3))
    return cnt_1 * cnt_3


def part2(inp):
    sorted_inp = sorted(inp)
    sorted_inp.insert(0, 0)
    sorted_inp.append(max(sorted_inp) + 3)
    difference_list = []

    for curr_element in sorted_inp[1:]:
        difference_list.append(curr_element - sorted_inp[sorted_inp.index(curr_element) - 1])

    result = 1
    count_1 = 0

    for diff_ele in difference_list:
        if diff_ele == 3:
            if count_1 == 2:
                result *= 2
            elif count_1 == 3:
                result *= 4
            elif count_1 == 4:
                result *= 7
            count_1 = 0
        else:
            count_1 += 1

    return result


print(part1(puzzleInput))
print(part2(puzzleInput))
