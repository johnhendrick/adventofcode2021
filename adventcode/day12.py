from adventcode.utils import read_file

file_path = './input/day12sample.txt'


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
print(links)
print(rooms)

# class CaveRooms:
#     def __init__(self, room, linked):
#         self.loc = room
#         self.linked = list()


def traverse(path=['start'], banned=['start']):
    next_rooms = links.get(path[-1])
    if set(next_rooms) == set(banned):
        return
    elif path[-1] == 'end':
        return 
    else:
        for room in next_rooms:

            traverse(path=path.append(room), banned)

            


