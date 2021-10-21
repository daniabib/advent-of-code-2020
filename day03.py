# 1 You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

# 2. start by counting all the trees you would encounter for the slope right 3, down 1

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
import numpy as np

with open('inputs/day03.txt') as f:
    field = np.array([line.strip().split("\n") for line in f])


def valid_pos(position, field=field):
    return position % len(field[0][0])


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_counts = []

for right, down in slopes:
    down_pos = 0
    side_pos = 0
    trees_count = 0
    for i in range(field.shape[0]):
        if down_pos <= field.shape[0] and field[down_pos][0][valid_pos(side_pos)] == '#':
            trees_count += 1
        down_pos += down
        side_pos += right
    trees_counts.append(trees_count)

print(np.prod(trees_counts))
