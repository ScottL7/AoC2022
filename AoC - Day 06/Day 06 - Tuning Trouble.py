# Advent of Code - Day 06 - Tuning Trouble

# Author: Scott Leitstein
# Date: Dec 6, 2022

# Puzzle Description: https://adventofcode.com/2022/day/6

import aoc_utility as util


def get_start_of_stream_pos(stream, len_marker):
    stream = str(stream)
    stream_len = len(stream)
    found = False
    end = False
    curr_start_pos = 0
    while not found and not end:
        found = len(set(stream[curr_start_pos:curr_start_pos+len_marker])) == len_marker
        curr_start_pos += 1
        if found:
            curr_start_pos += len_marker - 1
            break
        end = curr_start_pos + len_marker >= stream_len
    return curr_start_pos


data = util.get_input("day06-test.txt")
for row in data:
    print(f'Current start of stream position (marker len: 4): ({row}) {get_start_of_stream_pos(row, 4)}')
    print(f'Current start of stream position (marker len: 14): ({row}) {get_start_of_stream_pos(row, 14)}')

data = util.get_input("day06-puzzle.txt")[0]
print('*' * 30)
print(f'Current start of stream position: (code len: {len(data)}) (Marker len: 4) {get_start_of_stream_pos(data, 4)}')
print(f'Current start of stream position: (code len: {len(data)}) (Marker len: 14) {get_start_of_stream_pos(data, 14)}')
