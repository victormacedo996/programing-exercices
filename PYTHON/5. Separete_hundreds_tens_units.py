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


number = getInteger('Enter a number: ')
number = str(number)



if len(number) == 1:
    if int(number) > 1:
       print (f"{number} units")
    else:
        print(f"{number} unit")
    
elif len(number) == 2:
    if int(number[0]) > 1 and int(number[1]) > 1:
        print(f"{number[0]} tens and {number[1]} units")
    elif int(number[0]) == 1 and int(number[1]) > 1:
        print(f"{number[0]} ten and {number[1]} units")
    elif int(number[0]) > 1 and int(number[1]) == 1:
        print(f"{number[0]} tens and {number[1]} unit")
elif len(number) == 3:
    if int(number[0]) >= 1 and int(number[1]) >= 1 and int(number[2]) >= 1:
        print(f"{number[0]} hundreds, {number[1]} tens and {number[2]} units")
    elif int(number[0]) == 1 and int(number[1]) >= 1 and int(number[2]) >= 1:
        print(f"{number[0]} hundred, {number[1]} tens and {number[2]} units")
    elif int(number[0]) >= 1 and int(number[1]) <= 1 and int(number[2]) >= 1:
        print(f"{number[0]} hundreds, {number[1]} ten and {number[2]} units")
    elif int(number[0]) == 1 and int(number[1]) <= 1 and int(number[2]) >= 1:
        print(f"{number[0]} hundred, {number[1]} ten and {number[2]} units")
    elif int(number[0]) == 1 and int(number[1]) >= 1 and int(number[2]) <= 1:
        print(f"{number[0]} hundred, {number[1]} tens and {number[2]} unit")
    

lis = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

print('Separation of the list of numbers from the statement')

for item in lis:
    number = str(item)
    print(f"Number: {number}")
    if len(number) == 1:
        number = int(number)
        if number > 1:
           print(f"{number} units")
        else:
            print(f"{number} unit")
    elif len(number) == 2:
        tens = int(number[0])
        units = int(number[1])
        if tens >= 1 and units >= 1:
            print(f"{tens} tens and {units} units")
        elif tens == 1 and units >= 1:
            print(f"{tens} ten and {units} unit")
        else:
            print(f"{tens} ten and {units} unit")
    elif len(number) == 3:
        hundred = int(number[0])
        tens = int(number[1])
        units = int(number[2])
        if hundred >= 1 and tens >= 1 and units >= 1:
            print(f"{hundred} hundreds, {tens} tens and {units} units")
        elif hundred == 1 and tens >= 1 and units >= 1:
            print(f"{hundred} hundred, {tens} tens and {units} units")
        elif hundred >= 1 and tens <= 1 and units >= 1:
            print(f"{hundred} hundreds, {tens} ten and {units} units")
        elif hundred == 1 and tens <= 1 and units >= 1:
            print(f"{hundred} hundred, {tens} ten and {units} units")
        elif hundred == 1 and tens >= 1 and units <= 1:
            print(f"{hundred} hundred, {tens} tens and {units} unit")
    print('\n')