# Dice rolling game
import random
'''This is the basic one'''
while True:
    get_users_ans = input('Would you like to roll the dice? (y/n)')
    if get_users_ans.lower() == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif get_users_ans.lower() == 'n':
         print('Thank you!')
         break
    else:
        print('Invalid choice')

'''Here is the advanced one by me'''

'''import random

def number_of_dices(num_of_d):
    my_dices = [random.randint(1, 6) for n in range(num_of_d)]
    return my_dices
#The main function of this function is to find two random numbers within the range from 1 to 6
def number_of_rolls():
    rolls_counter = 0
    while True:
        user_num = input('Enter a number or(q) to finish: ')

        if user_num.lower() == 'q':
            print('Thank you')
            break

        if not user_num.isdigit():
            print('please enter a valid value')
            continue

        user_num = int(user_num)
        rolls = number_of_dices(num_of_d)
        rolls_counter += 1

        print(f'you rolled : {rolls}')
        print(f'The number of rolls so far: {rolls_counter}')

number_of_rolls()'''

