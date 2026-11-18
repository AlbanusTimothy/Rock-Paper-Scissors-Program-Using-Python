# ask the user to make a Choice
# if choice is not valid
# print error 
# let the computer to make a choice of its own
# print choices(emojis)
# determine the winner
# ask the user whether to continue or not
# if not
# terminate the game

import random

emojis={'r':'🥌','p':'📜','s':'✂'}
choices=('r','p','s')

while True:
    user_choice= input('Rock,Paper, or Scissors (r/p/s):').lower()
    if user_choice not in choices:
        print('invalid choice')
        continue

    computer_choice=random.choice(choices)

    print(f'you chose: {emojis[user_choice]}')
    print(f'the computer chose: {emojis[computer_choice]}')

    if user_choice== computer_choice:
        print('lol you tied with the computer!')
    elif (
        (user_choice=='r' and computer_choice=='s') or
        (user_choice== 's' and computer_choice=='p') or 
        (user_choice=='p' and computer_choice =='r')) :
        print('you win')
    else:
        print('you lost!')   

    user_continue=input('continue? (y/n)').lower()
    if user_continue=='n':
        break  






