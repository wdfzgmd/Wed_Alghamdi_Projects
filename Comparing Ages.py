from datetime import datetime

def calculate_age_and_birthday(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    birth_day_name = birthdate.strftime("%A")
    return age, birth_day_name

def authencational_date(date_string):
    try:

       year,month,day = map(int,date_string.split("-"))
       if year < 0 or month < 1 or month > 12 or day < 1 or day > 31:
           return False
       datetime.strptime(date_string, "%Y-%m-%d")
       return True
    except ValueError:
        return False

def validate_human():
    people = []

    while True:
        person_name = input("What is your name? (or type done to finish)")
        if person_name.lower() == 'done':
            break
        birthdate = input("What is your birthdate? (yyyy-mm-dd) ")
        if authencational_date(birthdate):
            age, birth_day_name = calculate_age_and_birthday(birthdate)
            people.append((person_name, age, birth_day_name))
        else:
            print("Sorry, your birthdate is invalid.")
    return people


def comparing(people):
    if len(people) == 1:
        print("There is no oldest or youngest person.")
        return

    ages = [person[1] for person in people]
    max_age = max(ages)
    min_age = min(ages)

    oldest_person = [person for person in people if person[1] == max_age][0]
    youngest_person = [person for person in people if person[1] == min_age][0]

    print(f"The oldest person is {oldest_person[0]} with age {oldest_person[1]}, born on a {oldest_person[2]}.")
    print(f"The youngest person is {youngest_person[0]} with age {youngest_person[1]}, born on a {youngest_person[2]}.")
    print(f"Total number of people: {len(people)}")


# Run the program
people = validate_human()
if people:
    comparing(people)





