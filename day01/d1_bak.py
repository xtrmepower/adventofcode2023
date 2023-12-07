import re

with open('d1_2.in', 'r') as file:
    raw_str = file.read()

    digit_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    # print(raw_str)
    for k in digit_dict.keys():
        raw_str = raw_str.replace(k, digit_dict[k])
    # print(raw_str)

    removed_alphabets_str = re.sub('[a-zA-Z]+', '', raw_str)
    lines = removed_alphabets_str.splitlines()
    # print(lines)

    result = 0
    for line in lines:
        line_length = len(line)

        print(f'line = {line}')
        val_pair_list = list(zip(line[::2], line[1::2]))
        print(val_pair_list)

        if line_length % 2 == 1:
            last_digit = line[-1]
            val_pair_list.append((last_digit, last_digit))
            print(f'amended_list = {val_pair_list}')

        for pair in val_pair_list:
            l, r = pair
            print(f'l = {l}, r = {r}')
            val_str = l + r
            val = int(val_str)
            print(f'val = {val}')
            result += val
            print(f'result = {result}')

        print(result)
