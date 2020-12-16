# with open('testInput.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = f.read()


def get_valid_number_ranges(inp):
    valid_number_ranges = []
    for valid_numbers in inp:
        valid_ranges = valid_numbers[valid_numbers.index(":") + 2:].split(" or ")
        for valid_range in valid_ranges:
            limit = valid_range.split("-")
            valid_number_ranges.append((int(limit[0]), int(limit[1])))
    return valid_number_ranges


def part1(inp):
    split_inp = inp.split("\n\n")
    valid_number_ranges = get_valid_number_ranges(split_inp[0].split("\n"))
    invalid_sum = 0

    for nearby_tickets_number in split_inp[2].split("\n"):
        if nearby_tickets_number.startswith("nearby tickets:"):
            continue
        for ticket_number in nearby_tickets_number.split(","):
            validated = False
            number = int(ticket_number)

            for valid_range in valid_number_ranges:
                lower_limit = valid_range[0]
                upper_limit = valid_range[1]
                if lower_limit <= number <= upper_limit:
                    validated = True
                    break
            if not validated:
                invalid_sum += number

    return invalid_sum


def part2(inp):
    

# invalid_tickets_number = []
# split_inp = inp.split("\n\n")
# valid_number_ranges = []
# valid_number_fields = []
# for valid_numbers in split_inp[0].split("\n"):
#     valid_ranges = valid_numbers[valid_numbers.index(":") + 2:].split(" or ")
#     for valid_range in valid_ranges:
#         valid_number_fields.append(valid_numbers[:valid_numbers.index(":")])
# 
#         limit = valid_range.split("-")
#         valid_number_ranges.append((int(limit[0]), int(limit[1])))
# 
# for nearby_tickets_number in split_inp[2].split("\n"):
#     if nearby_tickets_number.startswith("nearby tickets:"):
#         continue
#     for ticket_number in nearby_tickets_number.split(","):
#         validated = False
#         number = int(ticket_number)
# 
#         for valid_range in valid_number_ranges:
#             lower_limit = valid_range[0]
#             upper_limit = valid_range[1]
#             if lower_limit <= number <= upper_limit:
#                 validated = True
#                 break
#         if not validated:
#             invalid_tickets_number.append(nearby_tickets_number)
# 
# # store possible field at index
# possible_fields = {}
# for nearby_tickets_number in split_inp[2].split("\n"):
#     if nearby_tickets_number.startswith("nearby tickets:") or nearby_tickets_number in invalid_tickets_number:
#         continue
#     for idx_field, ticket_number in enumerate(nearby_tickets_number.split(",")):
#         number = int(ticket_number)
# 
#         for idx, valid_range in enumerate(valid_number_ranges):
#             lower_limit = valid_range[0]
#             upper_limit = valid_range[1]
#             if lower_limit <= number <= upper_limit:
#                 possible_fields_key = valid_number_fields[idx] + "-" + str(idx)
#                 if possible_fields_key in possible_fields:
#                     possible_fields[possible_fields_key] += 1
#                 else:
#                     possible_fields[possible_fields_key] = 0
# 
# # filtered_dict = {k: v for (k, v) in possible_fields.items() if k.startsWith('departure location')}
# departure_location_dict = {k: v for k, v in possible_fields.items() if k.startswith("departure location")}
# departure_station_dict = {k: v for k, v in possible_fields.items() if k.startswith("departure station")}
# departure_platform_dict = {k: v for k, v in possible_fields.items() if k.startswith("departure platform")}
# departure_track_dict = {k: v for k, v in possible_fields.items() if k.startswith("departure track")}
# departure_date_dict = {k: v for k, v in possible_fields.items() if k.startswith("departure date")}
# departure_time_dict = {k: v for k, v in possible_fields.items() if k.startswith("departure time")}
# 
# departure_list = [departure_location_dict, departure_station_dict, departure_platform_dict, departure_track_dict,
#                   departure_date_dict, departure_time_dict]
# probably_dep_fields = []
# for departure_list_entry in departure_list:
#     key_departure = max(departure_list_entry)
#     dash_idx = key_departure.index("-") + 1
#     probably_dep_fields.append(int(key_departure[dash_idx:]))
# 
# for ma_ticket in split_inp[1].split("\n"):
#     if ma_ticket.startswith("your ticket:"):
#         continue
#     ma_ticket_fields = ma_ticket.split(",")
#     product = 1
#     for field in probably_dep_fields:
#         product *= int(ma_ticket_fields[field])
#     return product


print(part1(puzzleInput))
print(part2(puzzleInput))
