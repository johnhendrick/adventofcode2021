import numpy as np
from adventcode.utils import read_file

file_path = './input/day11.txt'


def parse_file(file_content=read_file(file_path)):
    rows = file_content.split('\n')
    rows = [list(map(int, list(row))) for row in rows]
    return rows


def flash(arr, flash_count=0):
    if np.all(arr <= 9):
        return arr, flash_count
    else:
        # update surrounding
        new_flash_coor = np.nonzero(arr > 9)
        arr[new_flash_coor] = 0
        flash_count += len(new_flash_coor[0])
        for x, y in zip(new_flash_coor[0], new_flash_coor[1]):

            surrounding = [(x-1, y), (x-1, y+1), (x, y+1),
                           (x+1, y+1), (x+1, y), (x+1, y-1),
                           (x, y-1), (x-1, y-1)
                           ]
            for ele in surrounding:
                if ele[0] in range(arr.shape[0]) \
                    and ele[1] in range(arr.shape[1]) \
                        and arr[ele] != 0:
                    arr[ele] += 1

        arr, flash_count = flash(arr, flash_count=flash_count)

        return arr, flash_count


data = np.array(parse_file())

flash_count = 0
for i in range(100):
    data += 1
    data, flash_count = flash(data, flash_count=flash_count)

print(flash_count)

# part 2
data = np.array(parse_file())
j = 0
while np.any(data > 0):
    j += 1
    data += 1
    data, _ = flash(data)

print(j)
