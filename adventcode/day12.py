from adventcode.utils import read_file
from collections import Counter
import numpy as np

file_path = './input/day12.txt'


def parse_file(file_content=read_file(file_path)):
    rows = file_content.split('\n')
    pairs = [tuple(row.split('-')) for row in rows]
    rooms = dict()
    for row in rows:
        temp = row.split('-')
        for ele in temp:
            rooms[ele] = []

    for pair in pairs:
        rooms[pair[0]].append(pair[1])
        rooms[pair[1]].append(pair[0])

    return rooms, list(rooms.keys())


links, rooms = parse_file()
all_paths = []


def clean_blocked(lower_visted, max_):
    counts = Counter(lower_visted)
    exclude = ['start', 'end']
    output = []

    max_visit_hit = np.any(np.array(list(counts.values())) == max_)

    for ele in lower_visted:
        if ((ele in exclude) or max_visit_hit) and ele.islower():
            output.append(ele)

    return output


def traverse(path=[], step='start', visited=[], blocked=[], max_=1):
    path = path + [step]
    if step.islower():
        visited = visited + [step]
        blocked = clean_blocked(visited, max_)
    next_rooms = [room for room in links.get(step) if room not in blocked]

    if step == 'end':
        all_paths.append(path)
        return 1
    elif len(next_rooms) == 0:
        return 0
    else:
        count = 0
        for next_ in next_rooms:
            count += traverse(path=path, step=next_,
                              visited=visited, blocked=blocked, max_=max_)

        return count


unique_paths = traverse()

# print(all_paths)
print(unique_paths)

#  part 2
all_paths = []
unique_paths_v2 = traverse(max_=2)
print(unique_paths_v2)
