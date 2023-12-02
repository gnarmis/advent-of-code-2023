import os

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

possible_map = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def possible_game(draws: list[list[tuple]]) -> bool:
    """returns whether a game is possible
    
    eg of draws: 
    [[(1, "blue"), (4, "green")], 
    [(7, "blue"), (1, "red"), (14, "green")],
    ...]"""

    for subset in draws:
        for color_cubes in subset:
            if color_cubes[1] not in possible_map:
                raise RuntimeError("unknown color")
            if int(color_cubes[0]) > possible_map[color_cubes[1]]:
                return False
    return True


def power_of_game(draws: list[list[tuple]]) -> int:
    """returns the product of the min possible number of cubes
    of each color in the given game draws
    
    eg of draws: 
    [[(1, "blue"), (4, "green")], 
    [(7, "blue"), (1, "red"), (14, "green")],
    ...]
    """
    max_map = {}
    for subset in draws:
        for color_cubes in subset:
            if color_cubes[1] not in possible_map:
                raise RuntimeError("unknown color")
            if color_cubes[1] not in max_map:
                max_map[color_cubes[1]] = color_cubes[0]
            elif color_cubes[1] in max_map:
                # if it's larger, mark that as the new max
                if int(color_cubes[0]) > int(max_map[color_cubes[1]]):
                    max_map[color_cubes[1]] = int(color_cubes[0])
    return int(max_map["red"]) * int(max_map["green"]) * int(max_map["blue"])



possible_games_running_sum = 0
running_sum_of_powers = 0
with open(input_file, 'r') as f:
    for i, line in enumerate(f):
        # basic validation
        line_num = i + 1
        if line_num > 100:
            # definitely done at this point
            break
        game_index_prefix = f"Game {line_num}:"
        if game_index_prefix not in line:
            # import pdb; pdb.set_trace()
            raise RuntimeError("weird territory")
        
        # assemble draws for this game
        draws_str = line.split(game_index_prefix)[-1].strip()
        subset_strs = [item.strip() for item in draws_str.split(";")]
        draws = []
        for subset_str in subset_strs:
            color_cube_strs = [item.strip() for item in subset_str.split(", ")]
            output_subsets = []
            for color_cube_str in color_cube_strs:
                num, color = [item.strip() for item in color_cube_str.split(" ")]
                output_subsets.append((num, color))
            draws.append(output_subsets)
        
        if possible_game(draws):
            print(f"{game_index_prefix} is possible")
            possible_games_running_sum += line_num
        
        # part two: product of min num of cubes of each color
        power = power_of_game(draws)
        print(f"power of {game_index_prefix} is {power}")
        running_sum_of_powers += power

print(f"possible games indices sum={possible_games_running_sum}")
print(f"sum of powers={running_sum_of_powers}")
