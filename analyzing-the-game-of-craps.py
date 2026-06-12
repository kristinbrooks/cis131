"""
    script: analyzing-the-game-of-craps.py
    action: simulates playing 1,000,000 games of craps and prints out stats when finished
    author: Kristin Brooks
    date: 06/11/26
"""

import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)


wins = {}
losses = {}
num_games = 1000000

for game in range(num_games):
    die_values = roll_dice()    # first roll
    number_of_rolls = 1
    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7,11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2,3,12):   # lose
        game_status = 'LOST'
    else:   # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        number_of_rolls += 1
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:     # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:      # lose by rolling 7
            game_status = 'LOST'

    if game_status == 'WON':
        wins[number_of_rolls] = wins.get(number_of_rolls, 0) + 1
    else:
        losses[number_of_rolls] = losses.get(number_of_rolls, 0) + 1

# calculate and display results
total_wins = sum(wins.values())
total_losses = sum(losses.values())
print(f'Percentage of wins: {total_wins/num_games * 100:.1f}%')
print(f'Percentage of losses: {total_losses/num_games * 100:.1f}%')
print()
print(f'{"% Resolved":>19}{"Cumulative %":>19}')
print(f'{"Rolls":<8}{"on this roll":<16}of games resolved')
all_rolls = sorted(set(wins) | set(losses))
cumulative_percent = 0
for rolls in all_rolls:
    count = wins.get(rolls, 0) + losses.get(rolls, 0)
    percent_count = count/num_games * 100
    cumulative_percent += percent_count
    print(f'{rolls:<8}{f"{percent_count:.2f}%":>9}{f"{cumulative_percent:.2f}%":>18}')
