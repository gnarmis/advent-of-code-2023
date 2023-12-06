import functools
import numpy as np
import os
import re

dirname = os.path.dirname(__file__)
sample_file = os.path.join(dirname, "sample.txt")
input_file = os.path.join(dirname, "input.txt")

grid = []
line_strings = []
number_spans = []
star_spans = []
with open(input_file, "r") as f:
    for line in f:
        # pad first and last column
        padded_line = "." + line + "."
        # char-by-char grid
        char_row = []
        for char in padded_line:
            char_row.append(char)
        grid.append(char_row)

        # store each line as a string in a collection
        line_strings.append(padded_line)

        # fill out spans (eg: (0,3)) where numbers exist
        number_span_row = [match.span() for match in re.finditer(r"\d+", padded_line)]
        numbers = [padded_line[span[0]:span[1]] for span in number_span_row]
        
        # * spans
        star_span_row = [match.span() for match in re.finditer(r"\*", padded_line)]
        
        print(f"for '{padded_line=}': {numbers=}, {star_span_row=}")
        number_spans.append(number_span_row)
        star_spans.append(star_span_row)

    # pad top and bottom rows too
    row_len = len(grid[0])
    grid = [["."] * row_len] + grid + [["."] * row_len]
    line_strings = [["."] * row_len] + line_strings + [["."] * row_len]
    number_spans = [[None] * row_len] + number_spans + [[None] * row_len]
    star_spans = [[None] * row_len] + star_spans + [[None] * row_len]


def _valid_grid(arr: np.array, num_chars: set) -> bool:
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] in num_chars:
                continue
            elif arr[i][j] != "." and arr[i][j] != "\n" and bool(re.search(r"\D", arr[i][j])):
                return True
            else:
                continue
    return False


# allows easy slicing to debug/view parts
np_grid = np.array(grid)
neighbor_locations = []
part_one_sum = 0
for line_idx, number_span_rows in enumerate(number_spans):
    for number_span in number_span_rows:
        row_index = line_idx
        if row_index >= len(line_strings):
            continue
        if number_span is None:
            continue
        number = line_strings[row_index][number_span[0]:number_span[1]]
        number_chars = grid[row_index][number_span[0]:number_span[1]]
        print(f"{number_span=}, {number=}, {number_chars=}")

        grid_slice = np_grid[row_index-1:row_index+2, number_span[0]-1:number_span[1]+1]
        print(f"grid_slice={[(row_index-1,row_index+2), (number_span[0]-1,number_span[1]+1)]}")
        print(grid_slice)

        # search grid slice
        if _valid_grid(grid_slice, set(number_chars)):
            print(f"+{number}")
            part_one_sum += int(number)
        else:
            print(f"ignore {number}")

print(f"{part_one_sum=}")

# do two different number spans lie adjacent?
def _is_num_adjacent(span: tuple, num_span: tuple[tuple]) -> bool:
    print(f"{span=}, span_c={np_grid[row_index][span[0]]}, {num_span=}, num={line_strings[num_span[0]][num_span[1][0]:num_span[1][1]]}")
    one_col_is_adjacent = None
    for col in range(num_span[1][0], num_span[1][1]):
        print(f"{col=}, span[-]={span[0]} diff={abs(col - span[0])}")
        if abs(col - span[0]) <= 1:
            if one_col_is_adjacent is None:
                one_col_is_adjacent = True
    return bool(one_col_is_adjacent)

part_two_sum = 0
for line_idx, star_span_rows in enumerate(star_spans):
    for star_span in star_span_rows:
        if star_span is None:
            continue
        row_index = line_idx
        if row_index >= len(line_strings):
            continue

        grid_slice = np_grid[row_index-1:row_index+2, star_span[0]-1:star_span[1]+1]
        print(f"grid_slice={[(row_index-1,row_index+2), (star_span[0]-1,star_span[1]+1)]}")
        print(grid_slice)
        
        # find number spans in neighborhood. If exactly 2, multiply them.
        
        # (row, (start_col, stop_col)) for numbers in current and before/after rows as the star span
        nearby_number_spans = [(row_index-1, span) for span in number_spans[row_index-1]]
        nearby_number_spans.extend([(row_index, span) for span in number_spans[row_index]])
        nearby_number_spans.extend([(row_index+1, span) for span in number_spans[row_index+1]])
        print(f"{nearby_number_spans=}")

        adjacent_number_spans = [span for span in nearby_number_spans if _is_num_adjacent(star_span, span)]
        adjacent_numbers = [line_strings[span[0]][span[1][0]:span[1][1]] for span in adjacent_number_spans]
        if len(adjacent_numbers) == 2:
            adjacent_numbers_product = functools.reduce(lambda x, y: x*y, [int(num) for num in adjacent_numbers])
            part_two_sum += adjacent_numbers_product
            print(f"{adjacent_number_spans=}, {adjacent_numbers=}, {adjacent_numbers_product=}")
        else:
            print(f"ignoring; {adjacent_number_spans=}, {adjacent_numbers=}")

print(f"{part_two_sum=}")
