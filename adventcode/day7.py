import numpy as np
from utils import read_file

file_path = './input/day7.txt'


def parse_file(file_content):
    return [int(x) for x in file_content.split(',')]


def fuel(steps):
    return steps*(steps+1)/2


data = parse_file(read_file(file_path))

np_data = np.array(data)
median = np.median(np_data)

distance_sum = np.abs(np_data - median).sum()
print(distance_sum)

# part 2
simulation = []
possible_mid = list(range(min(np_data), max(np_data)+1))

for mid in possible_mid:
    fuel_req = fuel(np.abs(np_data-mid)).sum()
    simulation.append(fuel_req)

print('part 2 ', min(simulation))
