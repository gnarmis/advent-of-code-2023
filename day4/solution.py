import collections
import copy
import os
import re

dirname = os.path.dirname(__file__)
sample_file = os.path.join(dirname, 'sample.txt')
input_file = os.path.join(dirname, 'input.txt')

def get_numbers(file):
    cards = list(open(file))
    pairs_of_parts = [[re.findall(r"\d+", part) for part in card.split("|")] for card in cards]
    numbers = []
    #print(f"{pairs_of_parts=}")
    for pair in pairs_of_parts:
        numbers.append([pair[0][1:], pair[1]])
        #print(f"pair[0][1:]={pair[0][1:]}, pair[1]={pair[1]}")
    return numbers


def winning_matches_count(pair):
    return len(set(pair[1]) & set(pair[0]))
    

def score(pair):
    winning_matches = winning_matches_count(pair)
    if winning_matches < 1:
        card_score = 0
    else:
        card_score = 2 ** (winning_matches-1)
    print(f"{pair=}, {winning_matches=}, {card_score=}")
    return card_score


def part_one_total(file):
    return sum([score(p) for p in get_numbers(file)])

print(f"part one total = {part_one_total(input_file)}")


def scratchers(file):
    n = get_numbers(file)
    # [(card_index, wins_count), ...]
    m = [(i+1, winning_matches_count(p)) for i, p in enumerate(n)]
    print(f"{m=}")

    # copies tracker; init'd with 1 count for each original card
    copies = collections.Counter([item[0] for item in m])

    for i in range(m[-1][0]):
        wins_count = m[i][1]
        copies_count = copies[i+1]
        print(f"card={i+1}, {wins_count=}, {copies_count=}")
        # for next `wins_count` cards, increment each by `copies_count`
        for j in range(1, wins_count + 1):
            # i + 1 + j is the next card...
            #print(f"incrementing copies[{i + 1 + j}] from {copies[i + 1 + j]} to {copies[i + 1 + j] + copies_count}")
            copies[i + 1 + j] += copies_count
    return copies.total()

print(f"part two total = {scratchers(input_file)}")
