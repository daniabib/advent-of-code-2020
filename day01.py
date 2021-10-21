from itertools import product


def find_product(inputs):
    p = product(inputs, repeat=3)
    result = None

    for tuple in p:
        if result is None: 
            if tuple[0] + tuple[1] == 2020:
                result = tuple[0] * tuple[1]
        else:
            break

    return result


def find_product3(inputs):
    p = product(inputs, repeat=3)
    result = None

    for tuple in p:
        if result is None:
            if tuple[0] + tuple[1] + tuple[2] == 2020:
                result = tuple[0] * tuple[1] * tuple[2]
        else:
            break

    return result


with open('inputs/day01.txt') as f:
    inputs = [int(line.strip()) for line in f]

print(find_product3(inputs))
