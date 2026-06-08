# Number guessing game 
'''Libraries: Import random library
1- Welcome message.
2- create two input variables asking the user about the range
r1 = int(input()) - r2 = int(input())
3- set the range using a new variable range = random.randint(r1,r2)
4- create a limit for guessing which is 7
5- create a counter with the value = 0
6- create a loop as loong as the number of guessing is less than 7
7- ask the user to enter a number
8- state a condition, if the number is exactly what the random said, print that the answer is correct
9- if it is less than the half of the range print that your guess is too small
10- add one to the counter for each try'''

import random
print('''Welcome to guessing game\n We are so glad for having you today!!''')

number_of_guessing = random.randrange(100)

chances = 7
chances_counter = 0

while chances_counter <= chances:
    user_guess = int(input('Think about a number: '))
    if user_guess == number_of_guessing:
        print('Congratulations!\nYou got it right!!')
        break
    elif user_guess < number_of_guessing:
        print('Your guess is too small!\nTry again!')
    elif user_guess > 100:
        print('Enter a valid number!')
    
    chances_counter += 1

print(f'Number of chanses is {chances_counter}')
print(f'The number was {number_of_guessing}')
    

