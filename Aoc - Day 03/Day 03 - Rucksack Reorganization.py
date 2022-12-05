# Advent of Code - Day 03 - Rucksack Reorganization

# Author: Scott Leitstein
# Date: Dec 5, 2022

import aoc_utility as util
from itertools import zip_longest

DEBUG = False


def grouper(n, iterable, fillvalue=None):
    # ref: https://stackoverflow.com/questions/3415072/pythonic-way-to-iterate-over-sequence-4-items-at-a-time
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def get_sacks(filename):
    return util.get_input(filename)


def get_priority_time(sack):
    sack1 = set(list(sack[0:(len(sack)//2)]))
    sack2 = set(list(sack[len(sack)//2:]))

    return sack1.intersection(sack2)


def get_priority_total(sacks):
    total_priority = 0
    for sack in sacks:
        item = get_priority_time(sack)
        if len(item):
            item = item.pop()
            total_priority += (ord(item) - ord('A') + 27 if item.isupper() else ord(item) - ord('a') + 1)
        if DEBUG:
            if len(item) > 0:
                print(item)
            else:
                print('No Match Found...')
    return total_priority


def get_badge(sack1, sack2, sack3):
    return set(list(sack1)).intersection(set(list(sack2))).intersection(set(list(sack3)))


def get_badge_total(sacks):
    badge_total = 0
    for sack1, sack2, sack3 in grouper(3, sacks):
        badge = get_badge(sack1, sack2, sack3)
        if len(badge):
            badge = badge.pop()
            badge_total += (ord(badge) - ord('A') + 27 if badge.isupper() else ord(badge) - ord('a') + 1)
        if DEBUG:
            if len(badge) > 0:
                print(badge)
            else:
                print('No Match Found...')
    return badge_total


sacks = get_sacks("day03-test.txt")
print(f'Part1: (test) {get_priority_total(sacks)}')
print(f'Part2: (test) {get_badge_total(sacks)}')

sacks = get_sacks("day03-puzzle.txt")
print(f'Part1: (Puzzle) {get_priority_total(sacks)}')
print(f'Part2: (Puzzle) {get_badge_total(sacks)}')
