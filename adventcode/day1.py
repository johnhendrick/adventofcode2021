import pandas as pd

url = "https://adventofcode.com/2021/day/1/input"

data = pd.read_csv('./input/input.txt', names=['input'], sep='\n')
data_list = data.input.tolist()


def increase_count(data_list):
    """
    Args:
        data_list (list): input list

    Returns:
        int: number of increment
    """
    count = 0
    for i, ele in enumerate(data_list):
        if i < len(data_list)-1:
            if ele < data_list[i+1]:
                count += 1
            else:
                pass
    return count


count = increase_count(data_list)
print(count)

data['roll3'] = data.input.rolling(window=3).sum()
# part 2
print(increase_count(data.roll3.to_list()))
