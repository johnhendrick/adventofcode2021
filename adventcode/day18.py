# from adventcode.utils import read_file
import math
from copy import deepcopy

file_path = './input/day18.txt'


def parse_file(file_content):
    rows = file_content.split('\n')
    data = [eval(row) for row in rows]
    return data


sample = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""


def add(a, b):
    if a is None:
        return b
    return list([a]+[b])


def traverse_recurse(a, most_left=True, update=-99):
    if most_left:
        idx = 0
    else:
        idx = -1

    if isinstance(a, list):
        if isinstance(a[idx], int):
            a[idx] += update
        return traverse_recurse(a[idx], most_left=most_left, update=update)
    elif isinstance(a, int):
        return a


def _explode(a, depth=0, to_explode=[None, None], indexes=[], exploded_once=False, prev={}):

    flag = False

    if all([isinstance(ele, int) for ele in a]) and (depth == 4):
        if exploded_once:
            return a, to_explode, False, exploded_once
        else:
            to_explode = deepcopy(a)
            return a, to_explode, True, True

    else:
        for i, ele in enumerate(a):
            indexes.append(i)

            if isinstance(ele, list):
                ele, to_explode, flag, exploded_once = _explode(
                    ele, depth=depth+1, to_explode=to_explode, indexes=indexes, exploded_once=exploded_once, prev=prev)
                if flag:
                    a[i] = 0
                    flag = False
                    exploded_once = True
                    # print('explode')
            if (to_explode[0] is not None) or (to_explode[1] is not None):
                # peek left
                if to_explode[0] and (i-1 in range(len(a))):
                    if isinstance(a[i-1], list):
                        _ = traverse_recurse(
                            a[i-1], most_left=False, update=to_explode[0])
                    elif isinstance(a[i-1], int):
                        a[i-1] += to_explode[0]
                    to_explode[0] = None
                elif to_explode[0] and all([ele == 0 for ele in indexes]):
                    print('most_left ')
                    to_explode[0] = None
                elif to_explode[0] and all([ele == 0 for ele in indexes]) is False:
                    prev_ele = None
                    check = depth-1
                    while prev_ele is None and depth >= 0:
                        prev_ele = prev.get(check)
                        check -= 1
                    val = prev_ele[0][prev_ele[1]]
                    print('prev ele found, ', val)
                    if type(val) is list:
                        _ = traverse_recurse(
                            val, most_left=False, update=to_explode[0])
                    elif type(val) is int:
                        prev_ele[0][prev_ele[1]] += to_explode[0]
                    to_explode[0] = None

                # peek right
                if to_explode[1] and (i+1 in range(len(a))):
                    if isinstance(a[i+1], list):
                        _ = traverse_recurse(
                            a[i+1], most_left=True, update=to_explode[1])

                    elif isinstance(a[i+1], int):
                        a[i+1] += to_explode[1]
                    to_explode[1] = None
            prev[depth] = [a, i]
        return a, to_explode, flag, exploded_once


def removeElements(array, remove_elements):
    out = []
    for element in array:
        if isinstance(element, list):
            if None not in element:
                out.append(removeElements(element, remove_elements))
            else:
                print('beep')
                out.append(0)
        else:
            if element not in remove_elements:
                out.append(element)

    return out


def nested_clean(L):
    """Recursively remove list of length 1

    Args:
        L (list): list to be cleaned
    """
    for i, element in enumerate(L):
        if type(element) is list:
            if len(element) == 1:
                L[i] = 0
            else:
                nested_clean(element)


def explode(a):
    prev = None
    curr = a
    while prev != curr:
        prev = deepcopy(curr)
        curr, _, _, _ = _explode(curr)
    return curr


first = [True]


def split_(L):
    for i, element in enumerate(L):
        if type(element) is list:
            found = split_(element)
            if found:
                return True
        elif type(element) is int:
            if element > 9:
                L[i] = [element//2, math.ceil(element/2)]
                return True
                # split_(L[i])


def reduce_(data):
    prev = None
    for i, row in enumerate(data):
        curr = add(prev, row)
        print('post add:\n', curr)
        while prev != curr:
            prev = deepcopy(curr)
            curr = explode(deepcopy(curr))
            print('post explode:\n', curr)
            _ = split_(curr)
            print('post split:\n', curr)
    return curr


def magnitude(a, total=0):
    if all([isinstance(ele, int) for ele in a]):
        total = 3*a[0] + 2*a[1]
        return total
    else:
        for i, ele in enumerate(a):
            if isinstance(ele, list):
                a[i] = magnitude(ele)
        total += magnitude(a)

    return total

# reduce_
