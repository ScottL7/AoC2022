# Advent of Code - Day 04 - Camp Cleanup

# Author: Scott Leitstein
# Date: Dec 5, 2022

# Puzzle Description: https://adventofcode.com/2022/day/4

import aoc_utility as util


def get_pairs(filename):
    return util.get_input(filename)


def range_subset(range1, range2):
    # Ref: https://stackoverflow.com/questions/32480423/how-to-check-if-a-range-is-a-part-of-another-range-in-python-3-x
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2


def total_pair_ranges_overlaps(pairs_list):
    # Determine if the two pairs of ranges overlap
    total_pairs = 0
    for pairs in pairs_list:
        pair1 = range(int(pairs.split(',')[0].split('-')[0]), int(pairs.split(',')[0].split('-')[1]) + 1)
        pair2 = range(int(pairs.split(',')[1].split('-')[0]), int(pairs.split(',')[1].split('-')[1]) + 1)
        if range_subset(pair1, pair2) or range_subset(pair2, pair1):
            total_pairs += 1
    return total_pairs


def total_pair_overlaps(pairs_list):
    # Determine if the pair of ranges overlap at all - does not have to be the entire range
    total_overlaps = 0
    for pairs in pairs_list:
        pair1 = range(int(pairs.split(',')[0].split('-')[0]), int(pairs.split(',')[0].split('-')[1]) + 1)
        pair2 = range(int(pairs.split(',')[1].split('-')[0]), int(pairs.split(',')[1].split('-')[1]) + 1)
        found = False
        for pair_range_pos in pair1:
            found = pair_range_pos in pair2
            if found:
                total_overlaps += 1
                break

    return total_overlaps


pairs_list = get_pairs("day04-test.txt")
print(f'Num Pairs: (test) {len(pairs_list)}')
print(f'Overlapped range pairs (test): {total_pair_ranges_overlaps(pairs_list)}')
print(f'# of overlaps pairs (test): {total_pair_overlaps(pairs_list)}')


pairs_list = get_pairs("day04-puzzle.txt")
print('*' * 30)
print(f'Num Pairs: (puzzle) {len(pairs_list)}')
print(f'Overlapped pairs (puzzle): {total_pair_ranges_overlaps(pairs_list)}')
print(f'# of overlaps pairs (puzzle): {total_pair_overlaps(pairs_list)}')
