with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def part1(inp):
    right_password = 0
    for strInput in inp:
        splitted_by_space = strInput.split(' ')
        min_max_range = splitted_by_space[0]
        letter_with = splitted_by_space[1]
        letter = letter_with[0]
        string_to_check = splitted_by_space[2]

        splitted_min_max_range = min_max_range.split('-')
        min_range = int(splitted_min_max_range[0])
        max_range = int(splitted_min_max_range[1])

        cnt = 0
        for character in string_to_check:
            if character == letter:
                cnt = cnt + 1
        if min_range <= cnt <= max_range:
            right_password = right_password + 1
    print("Right password: " + str(right_password))


def part2(inp):
    right_password = 0
    for strInput in inp:
        splitted_by_space = strInput.split(' ')
        letter_with = splitted_by_space[1]
        letter = letter_with[0]
        string_to_check = splitted_by_space[2]
        positions = splitted_by_space[0]

        positions_array = positions.split('-')
        first = int(positions_array[0]) - 1
        second = int(positions_array[1]) - 1

        if (string_to_check[first] == letter) ^ (string_to_check[second] == letter):
            right_password = right_password + 1

    print("Right password: " + str(right_password))


# Part 1
part1(puzzleInput)
part2(puzzleInput)
