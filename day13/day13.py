# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]


def part1(inp):
    depart_time = int(inp[0])
    bus_list = inp[1].split(',')
    filtered_bus_list = [int(bus_id) for bus_id in bus_list if bus_id != "x"]

    stored_nearest_depart_time = 50
    stored_bus_id = 0

    for bus_id in filtered_bus_list:
        nearest_depart_time = ((depart_time // bus_id) + 1) * bus_id
        difference_nearest_depart_time = nearest_depart_time - depart_time
        if difference_nearest_depart_time < stored_nearest_depart_time:
            stored_nearest_depart_time = difference_nearest_depart_time
            stored_bus_id = bus_id
    return stored_nearest_depart_time * stored_bus_id


def part2(inp):
    bus_list = inp[1].split(',')
    dict_bus_list = {idx: int(bus_id) for idx, bus_id in enumerate(bus_list) if bus_id != "x"}
    result = 0
    step = 1

    for key, value in dict_bus_list.items():
        mod_remainder = (value - key) % value
        while result % value - mod_remainder != 0:
            result += step
        step *= value
    return result


print(part1(puzzleInput))
print(part2(puzzleInput))
