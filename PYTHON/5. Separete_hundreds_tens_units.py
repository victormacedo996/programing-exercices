"""
Make a Program that reads an integer less than 1000 and prints the number of hundreds, tens and units of it.

     Observing the plural terms the placement of the "e", the comma among others. Example:
     326 = 3 hundreds, 2 tens and 6 units
     12 = 1 dozen and 2 units Test with: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 and 16
"""

print('Exercice - separate the number of 3 digits into hundred, ten and unit ')

def getInteger(integer):
   while True:
       try:
           userInt = int(input(integer))
           if userInt >= 1000:
               print('number to large')
           else:
               return userInt
       except ValueError:
           print('You must enter an integer')

def separate_one_digit_number (number):
    if int(number) > 1:
       print (f"{number} units")
    else:
        print(f"{number} unit")
        
def separate_two_digit_number(number):
    if int(number[0]) > 1 and int(number[1]) > 1:
        print(f"{number[0]} tens and {number[1]} units")
    elif int(number[0]) <= 1 and int(number[1]) > 1:
        print(f"{number[0]} ten and {number[1]} units")
    elif int(number[0]) > 1 and int(number[1]) <= 1:
        print(f"{number[0]} tens and {number[1]} unit")
    else:
        print(f"{number[0]} ten and {number[1]} unit")

def separate_three_digit_number(number):
    if int(number[0]) > 1 and int(number[1]) > 1 and int(number[2]) > 1:
        print(f"{number[0]} hundreds, {number[1]} tens and {number[2]} units")
    elif int(number[0]) <= 1 and int(number[1]) > 1 and int(number[2]) > 1:
        print(f"{number[0]} hundred, {number[1]} tens and {number[2]} units")
    elif int(number[0]) <= 1 and int(number[1]) <= 1 and int(number[2]) > 1:
        print(f"{number[0]} hundred, {number[1]} ten and {number[2]} units")
    elif int(number[0]) <= 1 and int(number[1]) <= 1 and int(number[2]) <= 1:
        print(f"{number[0]} hundred, {number[1]} ten and {number[2]} unit")
    elif int(number[0]) > 1 and int(number[1]) <= 1 and int(number[2]) <= 1:
        print(f"{number[0]} hundreds, {number[1]} ten and {number[2]} unit")
    elif int(number[0]) > 1 and int(number[1]) > 1 and int(number[2]) <= 1:
        print(f"{number[0]} hundreds, {number[1]} tens and {number[2]} unit")
    elif int(number[0]) <= 1 and int(number[1]) > 1 and int(number[2]) <= 1:
        print(f"{number[0]} hundred, {number[1]} tens and {number[2]} unit")
    elif int(number[0]) > 1 and int(number[1]) <= 1 and int(number[2]) > 1:
        print(f"{number[0]} hundreds, {number[1]} ten and {number[2]} units")


number = getInteger('Enter a number: ')
number = str(number)

if len(number) == 1:
    separate_one_digit_number(number)
elif len(number) == 2:
    separate_two_digit_number(number)
elif len(number) == 3:
    separate_three_digit_number(number)
print('\n')

lis = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

print('Separation of the list of numbers from the statement')

for item in lis:
    number = str(item)
    print(f"Number: {number}")
    if len(number) == 1:
        separate_one_digit_number(number)
    elif len(number) == 2:
        separate_two_digit_number(number)
    elif len(number) == 3:
        separate_three_digit_number(number)
    print('\n')