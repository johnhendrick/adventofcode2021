import pandas as pd
from adventcode.utils import read_file

file_path = './input/day6.txt'


def parse_file(file_content):
    return [int(x) for x in file_content.split(',')]


def add_fish(population, timer=8):
    population.append(timer)


gang = parse_file(read_file(file_path))
#  attempt the question with list manipulation instead of class
days = 80
new_kid = 0
while days > 0:

    new_kid = 0
    for i, fish in enumerate(gang):
        if fish == 0:
            gang[i] = 6
            new_kid += 1
        elif fish:
            gang[i] -= 1
    [f(gang) for f in [add_fish]*new_kid]
    days -= 1

print('part 1 :', len(gang))

#  part 2
#  use dict instead
gang = parse_file(read_file(file_path))

population = pd.Series(gang).value_counts().to_dict()
for i in range(9):
    if population.get(i):
        pass
    else:
        population[i] = 0

days = 256
new_kids = 0
while days > 0:

    population = {k-1: v for k, v in population.items()}
    population[8] = new_kids
    population[6] = population[6] + new_kids

    new_kids = population[0]

    del population[-1]
    days -= 1

print('part2 :', sum(list(population.values())))
