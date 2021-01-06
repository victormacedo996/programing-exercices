"""
Create a program that take as input the name of the student and how many tests the semester 
had, calculate his mean and if he is approved or not
"""
from os import system

def getFloat(Float):
   while True:
       try:
           user_input = float(input(Float))
           if user_input < 0 or user_input > 10:
               print('The grade must be between 0 and 10')
           else:
               return user_input
       except ValueError:
           print('Use only numbers and separede decimals with point')

def getInteger(integer):
   while True:
       try:
           user_input = int(input(integer))
           return user_input
       except ValueError:
           print('You must enter a integer number')

def getAnswer (answer):
    while True:
        try:
            user_input = str((input(answer)).lower())
            if user_input != 'y' and user_input != 'n':
                print('Use only Y for yes and Y for no')
            else:
                return user_input
        except ValueError:
            print('You must enter a integer number')

all_students = {}

while True:
    system('clear')
    student_name = str(input('Enter the students name: '))
    i = 1
    grade_list = []
    while True:
        system('clear')
        if i == 1:
            r = f"{i}st"
        elif i == 2:
            r = f"{i}nd"
        elif i == 3:
            r = f"{i}rd"
        else:
            r = f"{i}th"
        grade = getFloat(f"Enter the {r} grade: ")
        grade_list.append(grade)
        i += 1
        answer = getAnswer('Enter another grade? ')
        if answer != 'y':
            break
        else:
            pass
    
    all_students[student_name] = grade_list
    answer = getAnswer ('Add another student? ')
    if answer != 'y':
        break
    else:
        pass

failed_students = []
approved_students = []
for key in all_students:
    mean = sum(all_students[key]) / len(all_students[key])
    if mean >= 7:
        print(f"Students: {key}, Mean: {round(mean, 2)}, Approved")
        approved_students.append(key)
    else:
        print(f"Students: {key}, Mean: {round(mean, 2)}, Failed")
        failed_students.append(key)

input('Press any key to see the list of approved students')
system('clear')
print('List of approved students:')
for item in approved_students:
    print(item)

input('Press any key to see the list of failed students')
system('clear')
for item in failed_students:
    print(item)