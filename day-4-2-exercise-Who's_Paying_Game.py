
"""
This game pickout a random card of a person who will pay for the bills of all his friends on an outing.
"""


import random

print()
names = input('Enter your full name and seperate them with commas.\n \n')
print()

# Friends names are splited and counted
names = names.split(', ')
people = len(names)

# Someone is picked at random to pay the bill
choice = random.randint(0, people -1)
person = names[choice]

decision = f'{person} is going to buy the meal today!'
print(decision)

print()
