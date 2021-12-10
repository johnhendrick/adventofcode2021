from adventcode.utils import read_file
import re

file_path = './input/day10.txt'


def parse_file(file_content=read_file(file_path)):
    rows = file_content.split('\n')
    return rows


data = parse_file()

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}
bracket_pairs = ['()', '[]', '{}', '<>']
pair_dict = {ele[0]: ele[1] for ele in bracket_pairs}


def scan(line, remove_left=True):
    while any(x in line for x in bracket_pairs):
        for br in bracket_pairs:
            line = line.replace(br, '')
    if remove_left:
        fault = re.sub(r'[([{<]', '', line)
    else:
        # extended for part2
        fault = line[::-1]
        for key in pair_dict.keys():
            fault = fault.replace(key, pair_dict[key])
        return fault
    return fault[0] if len(fault) > 0 else None


score = 0
incomplete_rows = []
for i, row in enumerate(data):
    found = scan(row)
    if found:
        score += scoring.get(found)
    else:
        incomplete_rows.append(i)
print(score)

# part 2
scoringv2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
collect = []
for pos in incomplete_rows:
    score2 = 0
    unmatched = scan(data[pos], remove_left=False)
    for ele in unmatched:
        score2 = score2*5 + scoringv2.get(ele)
    collect.append(score2)

print(sorted(collect)[round(len(collect)/2)])
