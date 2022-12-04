# Advent of Code - Day 01 - Counting Calories

# Author: Scott Leitstein
# Date: Dec 4, 2022


def get_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


# Part 1
def get_most_calories(filename):
    elves_list = get_data(filename)
    total = 0
    max_calories = 0
    for line in elves_list:
        if line == '\n':  # end of elf calorie list
            if total > max_calories:
                max_calories = total
            total = 0
            continue
        total += int(line.strip('\n'))
    return max_calories


# Part 1
print(get_most_calories('day01-test.txt'))
print(get_most_calories('day01-puzzle.txt'))

# ==================== #
# Part 2


def replace_smallest(value, top_3):
    for idx, i in enumerate(top_3):
        if value > top_3[idx]:
            top_3[idx] = value
            break
    return top_3.sort()


def get_top_3_most_calories(filename):
    elves_list = get_data(filename)
    top = [0, 0, 0]
    total = 0
    for line in elves_list:
        if line == '\n':  # end of elf calorie list
            replace_smallest(total, top)
            total = 0
            continue
        total += int(line.strip('\n'))
    replace_smallest(total, top)
    return sum(top)


# Part 2
print(get_top_3_most_calories('day01-test.txt'))
print(get_top_3_most_calories('day01-puzzle.txt'))
