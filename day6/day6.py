# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = f.read()


def part1(inp):
    question_answers = inp.split("\n\n")
    answered_yes = 0

    for group in question_answers:
        sanitized_str = str(group).replace("\n", "")
        set_dict = set(sanitized_str)
        answered_yes += len(set_dict)
    print(answered_yes)


def part2(inp):
    question_answers = inp.split("\n\n")
    answered_yes = 0
    for group in question_answers:
        group_size = len(group.split("\n"))
        sanitized_str = str(group).replace("\n", "")
        char_dictionary = dict.fromkeys(sanitized_str, 0)
        for c in sanitized_str:
            char_dictionary[c] += 1
            if group_size == char_dictionary[c]:
                answered_yes += 1

    print(answered_yes)


part1(puzzleInput)
part2(puzzleInput)
