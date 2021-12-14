from adventcode.utils import read_file
import re
import numpy as np

file_path = './input/day13.txt'


def parse_file(file_content=read_file(file_path)):
    rows = re.split(r'\n\n', file_content)
    steps = rows[1].split('\n')
    steps = [parse_isntruction(step) for step in steps]

    dots = rows[0].split('\n')
    dots = [tuple(line.split(',')) for line in dots]
    dots = [(int(loc[1]), int(loc[0])) for loc in dots]

    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])

    paper = np.zeros(shape=(max_x+1, max_y+1))
    for dot in dots:
        paper[dot] = 1
    return paper, steps


def parse_isntruction(text):
    x, y = None, None
    plane = re.search(r'(\S)=', text)[1]
    content = re.split(r'[xy]=', text)[-1]
    if plane == 'x':
        x = int(content)
    else:
        y = int(content)
    return (x, y)


def fold(fold, paper):
    # fold up
    if fold[1] and fold[0] is None:
        part1 = paper[:fold[1], :]
        part2 = np.flip(paper[fold[1]+1:, :], 0)

    # fold left
    if fold[0] and fold[1] is None:
        part1 = np.flip(paper[:, :fold[0]], 1)
        part2 = paper[:, fold[0]+1:]

    folded = part1 + part2
    folded[folded > 1] = 1
    return folded


paper, steps = parse_file()
paper = fold(steps[0], paper)
print((paper == 1).sum())

# part2
paper, steps = parse_file()
for step in steps:
    paper = fold(step, paper)
print(np.flip(paper, 1))
