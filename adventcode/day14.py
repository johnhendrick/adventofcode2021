from adventcode.utils import read_file
import re
from collections import Counter

file_path = './input/day14.txt'


def parse_file(file_content=read_file(file_path)):
    template, rules = re.split(r'\n\n', file_content)
    rules = {ele[0]: ele[1]
             for ele in [rule.split(' -> ') for rule in rules.split('\n')]}
    return template, rules


def insert(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]


def enrich(text):
    i = 0
    count = 0
    output = text
    while (i+2) < len(text)+1:
        substr = text[i:i+2]
        value = rules.get(substr)
        if value:
            output = insert(output, value, i+1+count)
            count += 1

        i += 1
    return output


template, rules = parse_file()
for i in range(10):
    template = enrich(template)
result = Counter(template)
print(max(result.values()) - min(result.values()))

# part 2
template, rules = parse_file()


def init_overlap(text):
    collect = []
    i = 0
    while (i+2) < len(text)+1:
        collect.append(text[i:i+2])
        i += 1
    return Counter(collect), Counter(text)


pair_count, char_count = init_overlap(template)
for i in range(40):
    curr_pair = pair_count.copy()
    for ele in list(curr_pair.keys()):
        if rules.get(ele):
            if pair_count.get(ele[0] + rules.get(ele)) is None:
                pair_count[ele[0] + rules.get(ele)] = 0
            if pair_count.get(rules.get(ele) + ele[1]) is None:
                pair_count[rules.get(ele) + ele[1]] = 0
            if char_count.get(rules.get(ele)) is None:
                char_count[rules.get(ele)] = 0

            pair_count[ele[0] + rules.get(ele)] += curr_pair[ele]
            pair_count[rules.get(ele) + ele[1]] += curr_pair[ele]
            pair_count[ele] -= curr_pair[ele]
            char_count[rules.get(ele)] += curr_pair[ele]

print(max(char_count.values()) - min(char_count.values()))
