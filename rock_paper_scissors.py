import random 

"""user_win=0
coupter_win=0

options=['rock','paper','scissors']



while True:
    user_input=input('Type Rock _ Paper _ Scissors _ Q to quit: ').lower()

    if user_input =='q':
        break

    if user_input not in  options:
       continue


    random_number=random.randint(0,2)
      
    random_pick=options[random_number]

    if user_input == 'rock' and random_pick =='scissors':
        print('You won!')
        user_win +=1
    
    elif user_input == 'scissors' and random_pick == 'paper':

        print('You won!')
        user_win +=1

    elif user_input == 'paper' and random_pick == 'rock':
         
         print('You won!')
         user_win +=1

    else:
        print('You lost!')
        coupter_win +=1
    
print('You wons', user_win,'times.')
print('Computer won',coupter_win,'times.')
print('Goodbye!')"""

#Game who say 10 is lost!
"""user_win=0
coutputer_win=0

lost=10

while True:
    user_input=input('type S To star to quit type Q : ')

    if user_input !='s':
        break

    x=1
    while True:

        random_pick=random.randint(1,2)
        x +=random_pick
        if x >= lost:
            print(f'Computer says {x}. You won!')
            user_win+=1
            break
        else:
            print(f'Computer {random_pick}\ncounter: {x}')

        user_option=int(input('Type number(1 or 2): '))
        if user_option not in [1,2]:
            print('Invalid choice! pick 1 or 2.')
            continue
        
        x +=user_option
        if x >= lost:
            print(f'You say {x}. Computer won!')
            coutputer_win +=1
            break
        else:
            print(f"Your:{user_option}\ncounter:{x}")

print(f'You won {user_win} times.')
print(f'Computer won on you {coutputer_win} times.')"""