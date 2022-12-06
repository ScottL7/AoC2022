# Advent of Code - Day 05 - Supply Stacks

# Author: Scott Leitstein
# Date: Dec 5, 2022

# Puzzle Description: https://adventofcode.com/2022/day/5

import aoc_utility as util

DEBUG = True


def get_data(filename):
    return util.get_input(filename)


def get_stack_arrangement(data):
    stacks = []
    num_stacks = 0
    stack_height = 0
    # Find the stack list row number
    for row, line in enumerate(data):
        if line[1:2] == '1':  # found stack number line
            stack_height = row
            num_stacks = int(line[-1])
            break

    # Init Stacks
    for row in range(num_stacks):
        stacks.append([])

    # Build Stacks
    for row in range(stack_height):
        line = data[row]
        # for idx, container in enumerate(range(len(line) // 3)):
        for idx, line_pos in enumerate(range(1, len(line), 4)):
            label = line[line_pos]
            if label != ' ':
                stacks[idx].append(label)
    return stacks


def move_containers(stacks, mover, num_to_move, origin, destination):
    for move in range(num_to_move):
        if mover == 9000:  # Part 1
            container = stacks[origin].pop(0)
            stacks[destination].insert(0, container)  # push
        else:  # Part 2
            container = stacks[origin][:num_to_move]  # extract all containers to move
            stacks[origin] = stacks[origin][num_to_move:]  # remove containers from the stack
            stacks[destination] = container + stacks[destination]
            break

    return stacks


def get_message(moves, stacks, mover):
    message = ""

    for move in moves:
        instructions = move.split(' ')
        num_containers = int(instructions[1])  # Number of containers to move
        starting_stack = int(instructions[3]) - 1
        dest_stack = int(instructions[5]) - 1
        stacks = move_containers(stacks, mover, num_containers, starting_stack, dest_stack)

    for stack in stacks:
        message += stack[0]
    return message


data = get_data("day05-test.txt")
stacks = get_stack_arrangement(data)
print(f'Message: (test) - CrateMover9000 {get_message(data[len(stacks)+1:], stacks, 9000)}')
stacks = get_stack_arrangement(data)
print(f'Message: (test) - CrateMover9001 {get_message(data[len(stacks)+1:], stacks, 9001)}')

data = get_data("day05-puzzle.txt")
stacks = get_stack_arrangement(data)
print(f'Message: (puzzle) - CrateMover9000 {get_message(data[len(stacks):], stacks, 9000)}')
stacks = get_stack_arrangement(data)
print(f'Message: (puzzle) - CrateMover9001 {get_message(data[len(stacks):], stacks, 9001)}')
