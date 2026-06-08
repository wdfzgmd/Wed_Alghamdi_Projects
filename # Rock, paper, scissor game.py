import random
print('''Welcome to 🪨📃✂️ game!\nWe are ready!''')
options = ['r','s','p']
rounds = int(input('How many rounds? '))
computer_points = 0
users_points = 0
the_round = 0

while the_round < rounds:
    
    user_choice = input('''Choose one of these options:
    'Rock': 'r' 
    'Paper': 'p' 
    'scissor':'s' ''')
    computer_choice = random.choice(options)
    if user_choice == 'r' and computer_choice == 's':
        users_points += 1
        print('You won this round')

    elif user_choice == 'r' and computer_choice == 'p':
        computer_points += 1
        print('The computer won this round')

    elif user_choice == 's' and computer_choice == 'p':
        users_points += 1
        print('You won this round')

    elif computer_choice == 'r' and user_choice == 's':
        computer_points += 1
        print('The computer won this round')

    elif computer_choice == 'r' and user_choice == 'p':
        users_points += 1
        print('You won this round')
    
    elif computer_choice == 's' and user_choice == 'p':
        computer_points += 1
        print('The computer won this round')
    
    elif computer_choice == 'r' and user_choice == 'r':
        print('No points')

    elif computer_choice == 's' and user_choice == 's':
        print('No points')

    elif computer_choice == 'p' and user_choice == 'p':
        print('No points')

    elif user_choice not in options:
        print('Enter a valid value!')
    
    the_round += 1


#comparing
if users_points > computer_points:
    print('Congratulations!\n You did it!!')
elif computer_points > users_points:
    print('Hard luck!')
else:
    print(f'Both of you got {computer_points}')


