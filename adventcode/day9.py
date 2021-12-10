from adventcode.utils import read_file

file_path = './input/day9.txt'


def parse_file(file_content=read_file(file_path)):
    rows = file_content.split('\n')
    return [list(row) for row in rows]


def get_value(hmap, x, y, pad=99):
    if x in range(xmax) and y in range(ymax):
        value = int(hmap[y][x])
    else:
        value = pad
    return value


hmap = parse_file()
xmax, ymax = len(hmap[0]), len(hmap)

collect = []
min_locs = []
for i in range(xmax):
    for j in range(ymax):
        ele = int(hmap[j][i])

        up = get_value(hmap, i, j-1) > ele
        down = get_value(hmap, i, j+1) > ele
        left = get_value(hmap, i-1, j) > ele
        right = get_value(hmap, i+1, j) > ele
        if up and down and left and right:
            collect.append(ele)
            min_locs.append((i, j))


print(sum(list(map(lambda x: x+1, collect))))

# part 2
explored_hmap = hmap.copy()


def traverse(x, y):
    if get_value(hmap, x, y) >= 9:
        # print('hit an edge')
        return 0
    else:
        moved = 1
        explored_hmap[y][x] = '9'
        moved += traverse(x, y-1)
        moved += traverse(x, y+1)
        moved += traverse(x-1, y)
        moved += traverse(x+1, y)
        return moved


sizes = []
for loc in min_locs:
    sizes.append(traverse(loc[0], loc[1]))
top_3 = sorted(sizes)[-3:]
print(top_3[0] * top_3[1] * top_3[2])
