path = "./input/day3.txt"

with open(path) as f:
    data = f.read().splitlines()


def count_ones(list_in):
    total = 0
    for item in list_in:
        total += int(item)
    return total


def string_bit_invert(string_in):
    return string_in.replace('1', '2').replace('0', '1').replace('2', '0')


n = len(data)
width = len(data[0])
half = n/2

stats = {pos: 0 for pos in range(width)}
# count
for row in data:
    for i in range(width):
        stats[i] = stats[i] + int(row[i])

# update stats
for key, value in stats.items():
    if value > half:
        stats[key] = 1
    else:
        stats[key] = 0

# collect metric
gamma = ''
for i in range(width):
    gamma += str(stats[i])

result = int(gamma, 2) * int(string_bit_invert(gamma), 2)
print('part1 : ', result)

############################################################
#  part 2


def get_most_common(total, half, invert=False):

    if total >= half:
        keep = 1
    else:
        keep = 0

    if invert:
        keep = (keep+1) % 2

    return str(keep)


def get_metric(data, i=0, invert=False):
    if len(data) == 1:
        return data[0]

    # count

    total = 0
    length = len(data)
    paths = {"1": [],  "0": []}
    for row in data:
        total = total + int(row[i])
        if row[i] == '1':
            paths['1'].append(row)
        else:
            paths['0'].append(row)

    mode = get_most_common(total, half=length/2, invert=invert)
    next_iter = paths[mode]
    return get_metric(next_iter, i=i+1, invert=invert)


oxy = get_metric(data)
co_two = get_metric(data, invert=True)

result2 = int(oxy, 2) * int(co_two, 2)
print('part2 :', result2)
