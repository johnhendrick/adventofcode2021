import pandas as pd

file_path = './input/input-d2.txt'
df = pd.read_csv(file_path, sep=r' ', names=['direction', 'scalar'])


def get_coor(df=df, aim=True):
    if aim:
        aim = 0
        h_pos = 0
        depth = 0
        for index, row in df.iterrows():
            if row.direction == 'forward':
                h_pos += row.scalar
                depth += aim*row.scalar
            elif row.direction == 'up':
                # depth -= row.scalar
                aim -= row.scalar
            elif row.direction == 'down':
                # depth += row.scalar
                aim += row.scalar

    else:
        loc_stats = df.groupby(by='direction').sum()
        h_pos = loc_stats.loc['forward'].item()
        depth = -loc_stats.loc['up'].item() + loc_stats.loc['down'].item()

    return h_pos * depth


# print(get_coor(aim=False))

#  part 2

print(get_coor())
