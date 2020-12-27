"""
Make a program that ask a number for the user and print the multiplication table
of this number
"""
def getFloat(Float):
    while True:
        try:
            user_input = float(input(Float))
            return user_input
        except ValueError:
            print('Use only numbers and separete decimals with point')

number = getFloat('Enter the number of the multiplication table: ')

for i in range(1, 11):
    print (f"{number} x {i} = {number * i}")
