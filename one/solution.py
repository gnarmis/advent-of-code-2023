"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

To play, please identify yourself via one of these services:

"""
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

"""
Your puzzle answer was 54597.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

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
