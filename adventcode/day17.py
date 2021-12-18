import re

file_path = './input/day15.txt'
sample = "target area: x=20..30, y=-10..-5"
input_ = "target area: x=14..50, y=-267..-225"


def parse_file(file_content=input_):
    x = re.search(r'x=(.*\d),', file_content).group(1).split('..')
    x = [int(ele) for ele in x]
    y = re.search(r'y=(.*\d)', file_content).group(1).split('..')
    y = [int(ele) for ele in y]
    return x, y


x1, y1 = parse_file(input_)


def dynamics(x=0, y=0, vx=0, vy=0):
    # simulate till landed
    top_y = y
    while x <= x1[1] and y >= y1[0]:
        prev = {'x': x, 'y': y,
                'vx': vx, 'vy': vy, 'max_y': top_y}
        x += vx
        y += vy
        if y > top_y:
            top_y = y
        vy -= 1
        if abs(vx) > 0:
            if vx > 0:
                vx -= 1
            if vx < 0:
                vx += 1
    if landed(prev):
        return prev
    else:
        return None


def max_x(vx):
    return vx*(1+vx)/2


def landed(params):
    return ((params['x'] >= x1[0]) and
            (params['x'] <= x1[1]) and
            (params['y'] >= y1[0]) and
            (params['y'] <= y1[1]))


param = {
    'vx': 7,
    'vy': None
}
top_y = 0
for vy_ in range(0, 1000):
    param['vy'] = vy_
    landing = dynamics(**param)
    if landing:
        if landing['max_y'] > top_y:
            top_y = landing['max_y']

print(top_y)

# part2
combination = 0
for vx_ in range(0, x1[1]+1):
    for vy_ in range(y1[0], 1000):
        param['vx'] = vx_
        param['vy'] = vy_
        landing = dynamics(**param)
        if landing:
            combination += 1
print(combination)
