# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


# F = 0 ; B = 1
# L = 0; R = 1

def convert_binary_to_int(binary):
    return int(binary, 2)


def swap_row_with_binary(text):
    return convert_binary_to_int(str(text).replace('F', '0').replace('B', '1'))


def swap_column_with_binary(text):
    return convert_binary_to_int(str(text).replace('L', '0').replace('R', '1'))


def calculate_seat_id(row, column):
    return row * 8 + column


def part1(inp):
    highest_seat_id = 0
    for strInput in inp:
        column = strInput[-3:]
        row = strInput[:7]
        row_as_number = swap_row_with_binary(row)
        column_as_number = swap_column_with_binary(column)
        seat_id = calculate_seat_id(row_as_number, column_as_number)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print(highest_seat_id)


def part2(inp):
    seat_id_list = []
    for strInput in inp:
        column = strInput[-3:]
        row = strInput[:7]
        row_as_number = swap_row_with_binary(row)
        column_as_number = swap_column_with_binary(column)
        seat_id = calculate_seat_id(row_as_number, column_as_number)
        seat_id_list.append(seat_id)

    sorted_list = sorted(seat_id_list)
    for seat_id in sorted_list[1:-1]:
        if seat_id - 1 not in sorted_list:
            print(seat_id - 1)
        if seat_id + 1 not in sorted_list:
            print(seat_id + 1)


part1(puzzleInput)
part2(puzzleInput)
