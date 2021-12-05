import numpy as np
from itertools import repeat

file_path = './input/day5.txt'


def read_file(file_path=file_path):
    with open(file_path) as f:
        return f.read()


def parse_file(file_content):
    collect = []
    row_split = file_content.split('\n')
    for row in row_split:
        start_end = row.split(' -> ')
        start_end = [tuple([int(x) for x in item.split(',')])
                     for item in start_end]
        collect.append(start_end)
    return collect


def move_2d(start, end):
    if start > end:
        step = -1
    else:
        step = 1
    return list(range(start, end, step))


def traverse_manhattan(left, right):
    # move x
    x_steps = move_2d(left[0], right[0])
    x_steps = list(zip(x_steps, repeat(left[1])))
    # move y
    y_steps = move_2d(left[1], right[1])
    y_steps = list(zip(repeat(left[0]), y_steps))

    return x_steps+y_steps+[right]  # add final destimation


def traverse_diagonal(left, right):

    x_steps = move_2d(left[0], right[0])
    y_steps = move_2d(left[1], right[1])
    steps = list(zip(x_steps, y_steps))

    return steps+[right]


def filter_h_v(coor_pair):
    """check if coor pair is going left or right.
    Also false where start coor == end coor

    Args:
        coor_pair (list of tuples)

    Returns:
        bool: True if coor is only vertical or horizontal travel
    """
    if ((coor_pair[0][0] == coor_pair[1][0]) ^
            (coor_pair[0][1] == coor_pair[1][1])):
        return True
    else:
        return False


coors = (parse_file(read_file()))
coors = [coor_pair for coor_pair in coors if filter_h_v(coor_pair)]

all_steps = []
for coor_pair in coors:
    steps_taken = traverse_manhattan(coor_pair[0], coor_pair[1])
    all_steps += steps_taken

# visualise in a numpy
visits = np.zeros((999, 999))
for step in all_steps:
    visits[step] += 1

visits = visits.T

print(np.count_nonzero(visits > 1))

# part2
coors = (parse_file(read_file()))
coors_m = [coor_pair for coor_pair in coors if filter_h_v(coor_pair)]
coors_diag = [
    coor_pair for coor_pair in coors if filter_h_v(coor_pair) is False]

all_steps = []
for coor_pair in coors_m:
    steps_taken = traverse_manhattan(coor_pair[0], coor_pair[1])
    all_steps += steps_taken
for coor_pair in coors_diag:
    diag_steps = traverse_diagonal(coor_pair[0], coor_pair[1])
    all_steps += diag_steps

# visualise in a numpy
visits2 = np.zeros((999, 999))
for step in all_steps:
    visits2[step] += 1

visits2 = visits2.T
print(np.count_nonzero(visits2 > 1))
