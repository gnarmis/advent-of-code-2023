import os
import re

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

running_sum = 0
with open(input_file, 'r') as f:
    for line in f:
        first_digit_groups = re.search(r"(\d)", line).groups()
        if len(first_digit_groups) != 1:
            raise RuntimeError(f"can't find first digit, line='{line}'")
        first_digit = first_digit_groups[0]
        last_digit_groups = re.search(r".*(\d)", line).groups()
        if len(last_digit_groups) != 1:
            raise RuntimeError(f"can't find last digit, line='{line}'")
        last_digit = last_digit_groups[0]
        two_digits = f"{first_digit}{last_digit}"
        two_digits_num = int(two_digits)
        #print(f"+{two_digits}")
        running_sum += two_digits_num

print(f"part one sum={running_sum}")

digits_map = {
    "1": "1",
    "one": "1",
    "2": "2",
    "two": "2",
    "3": "3",
    "three": "3",
    "4": "4",
    "four": "4",
    "5": "5",
    "five": "5",
    "6": "6",
    "six": "6",
    "7": "7",
    "seven": "7",
    "8": "8",
    "eight": "8",
    "9": "9",
    "nine": "9"
}

part_two_running_sum = 0
with open(input_file, 'r') as f:
    for line in f:
        first_digit_groups = re.search(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line).groups()
        if len(first_digit_groups) != 1:
            raise RuntimeError(f"can't find first digit, line='{line}'")
        first_digit_raw = first_digit_groups[0]
        first_digit = digits_map[first_digit_raw]
        last_digit_groups = re.search(r".*(\d|one|two|three|four|five|six|seven|eight|nine)", line).groups()
        if len(last_digit_groups) != 1:
            raise RuntimeError(f"can't find last digit, line='{line}'")
        last_digit_raw = last_digit_groups[0]
        last_digit = digits_map[last_digit_raw]
        two_digits = f"{first_digit}{last_digit}"
        two_digits_num = int(two_digits)
        #print(f"line='{line}', +{two_digits}")
        part_two_running_sum += two_digits_num

print(f"part two sum={part_two_running_sum}")
