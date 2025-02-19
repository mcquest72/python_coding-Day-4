# This program is a game called Rock, papper and scissors
# It uses randomisation to keep the game active.

import random

# using ascii art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print()
game_images = [rock, paper, scissors]

user_input = input('what do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n')

user_choice = int(user_input)
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print('Computer chose:')
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print('You win!')

elif computer_choice == 0 and user_choice == 2:
    print('You lose')

elif user_choice == 2 and computer_choice == 1:
    print('You win!')

elif computer_choice == 2 and user_choice == 1:
    print('You lose')

elif user_choice == 1 and computer_choice == 0:
    print('You win!')

elif computer_choice == 0 and user_choice == 1:
    print('You lose')

elif computer_choice == user_choice:
    print('It\'s a draw')

else: 
    print('You typed an invalid number, you lose!')

print()
