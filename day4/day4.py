import re

# with open('testInput.txt', 'r') as f:
# with open('valid.txt', 'r') as f:
# with open('invalid.txt', 'r') as f:
with open('puzzleInput.txt', 'r') as f:
    puzzleInput = f.read()

p = re.compile("^#[0-9a-f]{6}")
pid_regex = re.compile("^[0*\\d]{9}$")


def list_to_dict(rlist):
    return dict(map(lambda s: s.split(':'), rlist))


def validate_hcl(text):
    return p.match(str(text)) is not None


def validate_pid(text):
    return pid_regex.match(str(text)) is not None


def validate_hgt(text):
    try:
        height = str(text)
        number = int(height[:-2])
        if height.endswith("in"):
            return 59 <= number <= 76
        elif height.endswith("cm"):
            return 150 <= number <= 193
        return bool(False)
    except ValueError:
        return bool(False)


def part1(inp):
    passport_required = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    passport_to_check = inp.split("\n\n")
    valid_cnt = 0

    for passport_entry in passport_to_check:
        if all(x in passport_entry for x in passport_required):
            valid_cnt += 1

    print(valid_cnt)


def part2(inp):
    passport_required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ecl_valid_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    passport_to_check = inp.split("\n\n")
    valid_cnt = 0

    for passport_entry in passport_to_check:
        dict_passports = list_to_dict(passport_entry.split())

        # Check fields
        if all(x in dict_passports for x in passport_required):
            # additional validation
            valid_byr = len(dict_passports["byr"]) == 4 and 1920 <= int(dict_passports["byr"]) <= 2002
            valid_iyr = len(dict_passports["iyr"]) == 4 and 2010 <= int(dict_passports["iyr"]) <= 2020
            valid_eyr = len(dict_passports["eyr"]) == 4 and 2020 <= int(dict_passports["eyr"]) <= 2030
            valid_hgt = validate_hgt(dict_passports["hgt"])
            valid_hcl = validate_hcl(dict_passports["hcl"])
            valid_ecl = dict_passports["ecl"] in ecl_valid_values
            valid_pid = validate_pid(dict_passports["pid"])

            if valid_byr and valid_iyr and valid_eyr and valid_hgt and valid_hcl and valid_ecl and valid_pid:
                valid_cnt += 1
    print(valid_cnt)


part1(puzzleInput)
part2(puzzleInput)
