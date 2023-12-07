import re

with open('d1_1.in', 'r') as file:
    raw_str = file.read()

    removed_alphabets_str = re.sub('[a-zA-Z]+', '', raw_str)
    lines = removed_alphabets_str.splitlines()

    result = 0
    for line in lines:
        result += int(line[0] + line[-1])

    print(result)
