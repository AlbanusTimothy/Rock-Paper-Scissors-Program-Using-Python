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
def get_user_choice():
    while True:
     user_choice= input('Rock,Paper, or Scissors (r/p/s):').lower()
     if user_choice  in choices:
      return user_choice
     else:
        print('invalid choice')

def display_choices(user_choice,computer_choice):
   print(f'you chose: {emojis[user_choice]}')
   print(f'the computer chose: {emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
        if user_choice== computer_choice:
            print('lol you tied with the computer!')
        elif (
            (user_choice=='r' and computer_choice=='s') or
            (user_choice== 's' and computer_choice=='p') or 
            (user_choice=='p' and computer_choice =='r')) :
            print('you win')
        else:
            print('you lost!')  


def play_game():
    while True:
        user_choice=get_user_choice()
        computer_choice=random.choice(choices)
        display_choices(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)

        user_continue=input('continue? (y/n)').lower()
        if user_continue=='n':
            break                     
        
play_game()
  






