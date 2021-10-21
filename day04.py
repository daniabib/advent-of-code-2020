import re

REQ_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse(raw):
    passports = raw.strip().split('\n\n')
    pass_list = []
    for passport in passports:
        pass_dict = {}
        for entry in passport.split():
            (key, value) = entry.split(':')
            pass_dict[key] = value
        pass_list.append(pass_dict)

    return pass_list


def is_present(passport, required_fields=REQ_FIELDS):
    return all([field in passport.keys() for field in required_fields])


def check_byr(passport):
    return len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002


def check_iyr(passport):
    return len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020


def check_eyr(passport):
    return len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030


def check_hgt(passport):
    if 'cm' in passport['hgt']:
        value = int(passport['hgt'].split('c')[0])
        return 150 <= value <= 193
    elif 'in' in passport['hgt']:
        value = int(passport['hgt'].split('i')[0])
        return 59 <= value <= 76
    else:
        return False


def check_hcl(passport):
    return bool(re.match("^#[a-fA-F0-9_]{6}$", passport.get('hcl', '')))


def check_ecl(passport):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return sum([color in passport['ecl'] for color in valid_colors]) == 1


def check_pid(passport):
    return len(passport['pid']) == 9 and passport['pid'].isdigit()


def is_valid(passport):
    if is_present(passport):
        checks = [check_byr, check_iyr, check_eyr, check_hgt,
                  check_hcl, check_ecl, check_pid]
        return all([check(passport) for check in checks])
    else:
        return False


def count_valid(passports):
    return sum([is_valid(passport) for passport in passports])


with open("inputs/day04.txt") as f:
    passports_list = parse(f.read())
    print(count_valid(passports_list))
