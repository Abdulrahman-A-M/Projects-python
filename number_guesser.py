import random
top_for_range=input('Type a number for guesseing: ')

if top_for_range.isdigit():
    top_for_range=int(top_for_range)
    
    if top_for_range <= 0:
        print('Please type a number great than 0 next time')
        quit()
        
else:
    print('Please type a number next time.')
    quit()


random_number=random.randint(0,top_for_range)
guess=0

while True:
    guess +=1
    user_guess=input('Make a guess: ')

    if user_guess.isdigit():
        user_guess=int(user_guess)
    
    else:
        print("Please type a number next time!")
        continue
    

    if user_guess==random_number:
        print('You got it!')
        break
    
    else:
        if user_guess >random_number:
            print('You were above the number! :>')
        else:
            print('You were below the number! :)')


print('You got it',guess,'guesses!')

