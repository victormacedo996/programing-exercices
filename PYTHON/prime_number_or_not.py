"""
Make a program that take a integer input from the user, verify if it is a prime number
or not and 
"""

def getInteger(integer):
    while True:
        try:
            user_input = int(input(integer))
            return user_input
        except ValueError:
            print('You must enter a integer number')

number = getInteger('Enter a integer: ')

mult = 0

for i in range(2, number):
    if number % i == 0:
        print(f"Multiple of: {i}")
        mult += 1

if mult == 0:
    print('Prime number')
else:
    print(f"It has {mult} mutiples higher than 2 and minors than {number}")

print('\n')