import re


def count_correct_passwords(inputs):
    return sum([len(re.findall(letter, password)) >= int(lo) and
                len(re.findall(letter, password)) <= int(hi)
               for lo, hi, letter, _, password in inputs])


def count_correct_passwords2(inputs):
    return sum([(password[int(lo) - 1] == letter) ^ (password[int(hi) - 1] == letter)
                for lo, hi, letter, _, password in inputs])


with open('inputs/day02.txt') as f:
    inputs = [re.split('[\s\-:]', line.strip()) for line in f]

print(f"Correct passwords with policy one: {count_correct_passwords(inputs)}")
print(f"Correct passwords with policy two: {count_correct_passwords2(inputs)}")
