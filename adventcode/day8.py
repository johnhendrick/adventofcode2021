import numpy as np
from adventcode.utils import read_file
import copy

file_path = './input/day8.txt'


def parse_file(file_content):
    rows = file_content.split('\n')
    data = [row.split(' | ') for row in rows]
    for i, entry in enumerate(data):
        data[i][0] = entry[0].split()
        data[i][1] = entry[1].split()
    return data


data = parse_file(read_file(file_path))

l_mapping = {1: 2, 4: 4, 7: 3, 8: 7}

#  part 1
input_val = [row[0] for row in data]
output_val = [row[1] for row in data]

np_input = np.array(input_val)
np_output = np.array(output_val)
np_len = np.vectorize(len)(np_output)

print(np.isin(np_len, list(l_mapping.values())).sum())


# part 2
#    a'
#    _
#  f'|_| b'  inside: g'
#  e'|_| c'
#    d'

def length_search(np_array_in, size):
    # only for searching 1 4 7 8
    lengths = np.vectorize(len)(np_array_in)
    result = np_array_in[lengths == size]
    assert len(result) == 1
    return np_array_in[lengths == size].item()


def sort_string(a_string):
    sorted_characters = sorted(a_string)
    return "".join(sorted_characters)


collect = []
for i in range(len(input_val)):
    input_row = input_val[i]
    # print(length_search(np.array(input_row), l_mapping.get(1)))
    # start with decoding 1478
    decode = {num: length_search(np.array(input_row), l_mapping.get(num))
              for num in [1, 4, 7, 8]}
    size5 = [signal for signal in input_row if len(signal) == 5]
    size6 = [signal for signal in input_row if len(signal) == 6]

    decode[3] = [j for j in size5 if len(
        set(decode[8]) - set(j) - set(decode[1])) == 2][0]
    decode[6] = [j for j in size6 if len(
        set(decode[8]) - set(j) - set(decode[1])) == 0][0]
    decode[9] = [j for j in (set(size6)-set(decode[6]))
                 if len(set(j) - set(decode[3])) == 1][0]
    decode[0] = list(set(size6) - {decode[6]} - {decode[9]})[0]
    decode[5] = [j for j in (set(size5)-set(decode[3]))
                 if len(set(j) - set(decode[6])) == 0][0]
    decode[2] = list(set(size5) - {decode[5]} - {decode[3]})[0]

    for num in range(0, 10):
        assert isinstance(decode[num], str)

    inv_decode = {sort_string(v): k for k, v in decode.items()}
    assert len(decode) == 10
    assert len(inv_decode) == 10

    result = ''
    for ele in output_val[i]:
        result += str(inv_decode[sort_string(ele)])
    collect.append(int(result))

print('part 2 :', sum(collect))
