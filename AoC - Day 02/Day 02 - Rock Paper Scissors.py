# Advent of Code - Day 02 - Rock Paper Scissors

# Author: Scott Leitstein
# Date: Dec 4, 2022

"""
 Game Play Rules:
    Player 1 moves: A for Rock, B for Paper, and C for Scissors
    Player 2 moves: X for Rock, Y for Paper, and Z for Scissors

    1 for Rock, 2 for Paper, and 3 for Scissors - play values
    0 for lost, 3 for draw, and 6 for win       - game results values
"""

import aoc_utility as util

player_plays = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
pt2_player_plays = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 3, "Z": 6}

lost = 0
draw = 3
win = 6

#    R P S
#  R
#  P
#  S

pt1_game_play_rules = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

pt2_game_play_rules = [
    [3, 1, 2],
    [1, 2, 3],
    [2, 3, 1]
]


def get_game_plays(filename):
    return util.get_input(filename)


def get_pt1_total_score(game_plays):
    total_score = 0
    for play in game_plays:
        player1_play_pos = player_plays[play[0]]
        player2_play_pos = player_plays[play[2]]
        game_score = pt1_game_play_rules[player1_play_pos][player2_play_pos]
        if game_score == lost:
            total_score += player_plays[play[2]] + 1
        else:
            total_score += player_plays[play[2]] + game_score + 1
    return total_score


def get_pt2_total_score(game_plays):
    total_score = 0
    for play in game_plays:
        player1_play_pos = player_plays[play[0]]
        if pt2_player_plays[play[2]] == lost:
            total_score += pt2_game_play_rules[0][player1_play_pos]
        elif pt2_player_plays[play[2]] == draw:
            total_score += pt2_game_play_rules[1][player1_play_pos] + draw
        else:
            total_score += pt2_game_play_rules[2][player1_play_pos] + win
    return total_score


print(get_pt1_total_score(get_game_plays("day02-test.txt")))
print(get_pt1_total_score(get_game_plays("day02-puzzle.txt")))

print(get_pt2_total_score(get_game_plays("day02-test.txt")))
print(get_pt2_total_score(get_game_plays("day02-puzzle.txt")))
