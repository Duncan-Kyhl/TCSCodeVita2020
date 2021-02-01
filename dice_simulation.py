"""
### Dice Simulation ###
PROBLEM DESCRIPTION
    We know that a fair S-sided dice would show up one of the numbers 1 through S with equal probability (1/S) at each throw. We also know that a fair coin (a two-sided dice!) would show up heads and tails with equal probability (0.5) at each toss.
    Note: We may assume that a 2-sided dice (coin) is numbered 1 on a side and 2 on the other.

    Let's play the following game using different-sided dices:
        1) Throw a fair S-sided dice and note the number S1 shown. S1 would be a natural number in the closed interval [1, S].

        2) If S1 is 1, stop, else throw a fair S1-sided dice and note the number S2 shown. S2 would be a natural number in [1, S1].

        3) If S2 is 1, stop, else throw a fair S2-sided dice. S2 would be in [1, S2].

    Repeat in the above fashion, stopping if the previous throw is 1 or throwing a dice with a number of sides equal to the previous throw.

    Given number S and starting with step 1, what the expected number of dice throws in one play?

    Write a program to accept S, run a simulation of the game 10000 times and note the expected number of dice throws, averaging the number over the number of simulations. The average may be rounded off. Repeat the set of 10000 runs 9 more times and note the average numbers of dice throws in a game. Print the minimum of the rounded averages obtained from the 10 sets of simulations.

CONSTRAINTS
    0< S <=10^5

INPUT
    One line containing one integer representing S-sided dice

OUTPUT
    One integer containing expected number of dice throws rounded up to the nearest natural number (minimum average over 10 sets of 10000 game simulations)

TIME LIMIT
3

Examples
    Example 1
        Input = 2
        Output =2

    Example 2
        Input = 3
        Output = 2
"""
### variable number of rolls per game.
### 100-thousand game per match.

import random

print("Dice Simulator!")
print("How many sides are on your die?")
sides = int(input())

# number of rolls each game
game_log = []
# average rolls each match
match_log = []

def Average(lst): 
    return round(sum(lst) / len(lst))

for matches in range(10):
    for games in range(10000):
        # S = random.randint(1, 10e5)
        S = sides
        rolls = 0
        while True:
            if S == 1: # stop game
                break 

            else: # roll again
                S = random.randint(1, S)
                rolls += 1
        
        game_log.append(rolls)

    game_log_avg = Average(game_log)
    match_log.append(game_log_avg)

match_log_avg = Average(match_log)

print(f"Average number of rolls per match: {match_log_avg}")