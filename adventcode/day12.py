from adventcode.utils import read_file

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


def traverse(path=[], step='start', blocked=[]):
    path = path + [step]
    if step.islower():
        blocked = blocked + [step]
    next_rooms = [room for room in links.get(step) if room not in blocked]

    if step == 'end':
        all_paths.append(path)
        return 1
    elif len(next_rooms) == 0:
        return 0
    else:
        count = 0
        for next_ in next_rooms:
            count += traverse(path=path, step=next_, blocked=blocked)

        return count


unique_paths = traverse()

print(all_paths)
print(unique_paths)
