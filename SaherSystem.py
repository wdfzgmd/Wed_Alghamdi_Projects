# Reading the text file
def reading_file(file_name):
    read_me = open(file_name)
    splitted_by_line = read_me.readlines()
    read_me.close()
    return [[splitted_by_line[idx][:-1], int(splitted_by_line[idx+1])] for idx in range(0, len(splitted_by_line), 2)]

def display_all(the_splitted_list):
    print('All results are: ')
    for sublist in the_splitted_list:
        print(sublist)

def search_for(the_splitted_list):
    name_to_fetch = input('Write a name to search for: ')
    found_it = False
    for sublist in the_splitted_list:
        if name_to_fetch in sublist:
            found_it = True
            print(sublist)
    if not found_it:
        print('Sorry, the name is not found!')
        found_it = False


def add_modify_delete(the_splitted_list):
    user_choice = input('''Which one do you want?
    1. Add
    2. Modify
    3. Delete''')
    if user_choice == '1':
        user_name = input('Write a name to add it: ')
        user_val = int(input('Write a number of violations: '))
        the_splitted_list.append([user_name, user_val])
        print(f'{user_name} has been added successfully to the system!')

    elif user_choice == '2':
        user_name = input('Write a name to modify: ')
        repeated_names = [element for element in the_splitted_list if element[0] == user_name]
        print(f'We found the following for {user_name}: ')
        for idx, element in enumerate(repeated_names, 1):
            print(f'{idx} - {element[0]} {element[1]}')
        user_s_choice = int(input(f'Which one do you want in the range from (1, {len(repeated_names)})'))
        if user_s_choice >= 1 and user_s_choice <= len(repeated_names):
            new_val = int(input('Enter a new value: '))
            repeated_names[user_s_choice - 1][1] = new_val
            print(f'{user_name} has been added successfully to the system!')

    elif user_choice == '3':
        user_name = input('Write a name to delete: ')
        repeated_names = [element for element in the_splitted_list if element[0] == user_name]
        print(f'We found the following for {user_name}: ')
        for idx, element in enumerate(repeated_names, 1):
            print(f'{idx} - {element[0]} {element[1]}')
        user_s_choice = int(input(f'Which one do you want in the range from (1, {len(repeated_names)})'))
        if user_s_choice >= 1 and user_s_choice <= len(repeated_names):
            the_splitted_list.remove(repeated_names[user_s_choice - 1])
            print(f'{user_name} has been removed successfully from the system!')

def swap(the_splitted_list):
    return the_splitted_list[1]

def sorting(the_splitted_list):
    user_choice = input('Choose a number for sorting : [1] Increasing [2] Decreasing')
    if user_choice == '1':
        the_splitted_list.sort(key=swap)
    elif user_choice == '2':
        the_splitted_list.sort(key=swap, reverse=True)
    for sublist in the_splitted_list:
        print(sublist)

def main():
    the_splitted_list = reading_file('dataset.txt')
    print('Welcome to Saher System!')
    print('Be patient, we are uploding your information from Nafath!')
    while True:
        user_choice = input('''Choose one of the following options:
    1. Display all results
    2. Search for a name
    3. Add/modify/delete
    4. Sort names
    5. Exit''')
        if user_choice == '1':
            display_all(the_splitted_list)
        elif user_choice == '2':
            search_for(the_splitted_list)
        elif user_choice == '3':
            add_modify_delete(the_splitted_list)
        elif user_choice == '4':
            sorting(the_splitted_list)
        elif user_choice == '5':
            print('Thank you for using Saher System')
            the_latest_version = open('The_last_update.txt','w')
            the_latest_version.write(str(the_splitted_list))
            the_latest_version.close()
            break
        else:
            print('Invalid choice!')
main()
