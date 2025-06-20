import random


def roll():
    min_value = 1
    max_value =6
    roll=random.randint(min_value,max_value)
    return roll


while True:
    palyers=input("Enter the number of players (2 - 4)")
    if palyers.isdigit():
        palyers=int(palyers)
        if 2<= palyers <=4:
            break
        else:
            print('Must be between 2 - 4 players.')
    else:
        print('Invalid, try again.')

max_score = 50
players_score=[0 for _ in range(palyers)]


while max(players_score) <max_score:
    for player_idx in range(palyers):
        print('\nPlayer number',player_idx +1,'turn has just started!')
        print('Your total score is:',players_score[player_idx],'\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)')
            if should_roll.lower() !='y':
                break

            value=roll()
            if value ==1:
                print('You rolled a 1! Turn done!')
                current_score=0
                break
            else:
                current_score +=value
                print('You rolled a:',value)
            
            print('Your score is:',current_score)
            
            players_score[player_idx]+=current_score
            print('Your total score is:',players_score[player_idx])

max_score=max(players_score)
winning_idx=players_score.index(max_score)
print('Player number',winning_idx +1 , 'is the winner with a score of:',max_score)

