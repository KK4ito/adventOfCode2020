import itertools

# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = [str(x.strip()) for x in f]

direction_cycle = ["N", "E", "S", "W"]
degree_in_index = {0: 0,
                   90: 1,
                   180: 2,
                   270: 3,
                   360: 0
                   }


def part1(inp):
    current_direction = "E"
    dict_directions = {"N": 0,
                       "S": 0,
                       "E": 0,
                       "W": 0}

    for str_direction in inp:
        action = str_direction[0]
        action_value = int(str_direction[1:])

        if action == "F":
            action = current_direction
            dict_directions[action] += action_value

        elif action == "L" or action == "R":
            index_to_move = degree_in_index[action_value]
            if action == "L":
                new_index = direction_cycle.index(current_direction) - index_to_move
            else:
                new_index = direction_cycle.index(current_direction) + index_to_move - 4
            current_direction = direction_cycle[new_index]

        else:
            dict_directions[action] += action_value

    sum_n_s = abs(dict_directions["N"] - dict_directions["S"])
    sum_e_w = abs(dict_directions["E"] - dict_directions["W"])
    return sum_n_s + sum_e_w


def part2(inp):
    dict_directions = {"N": 0,
                       "S": 0,
                       "E": 0,
                       "W": 0}

    # using list to shift numbers, use direction_cycle as key indices
    waypoint_dict_directions = [1, 10, 0, 0]

    for str_direction in inp:
        action = str_direction[0]
        action_value = int(str_direction[1:])

        if action == "F":
            for waypoint_coord_direction, waypoint_coord_value in enumerate(waypoint_dict_directions):
                direction = direction_cycle[waypoint_coord_direction]
                if waypoint_coord_value == 0:
                    continue
                waypoint_coord_value *= action_value
                dict_directions[direction] += waypoint_coord_value

        elif action == "L" or action == "R":
            index_to_move = degree_in_index[action_value]
            if action == "L":
                for _ in itertools.repeat(None, index_to_move):
                    waypoint_dict_directions.append(waypoint_dict_directions.pop(0))
            else:
                for _ in itertools.repeat(None, index_to_move):
                    waypoint_dict_directions.insert(0, waypoint_dict_directions.pop())
        else:
            waypoint_dict_directions[direction_cycle.index(action)] += action_value

    sum_n_s = abs(dict_directions["N"] - dict_directions["S"])
    sum_e_w = abs(dict_directions["E"] - dict_directions["W"])
    return sum_n_s + sum_e_w


print(part1(puzzleInput))
print(part2(puzzleInput))
