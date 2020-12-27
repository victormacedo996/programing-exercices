"""
Make a program that ask for two numbers and print the integer numbers between these
two and the sum of them
"""

def getInteger(integer):
    while True:
        try:
            userInt = int(input(integer))
            return userInt
        except ValueError:
            print('You must enter an integer')


number1 = getInteger('Enter the first number: ')
number2 = getInteger('Enter the second number: ')
list_of_numbers = []


for i in range(number1 + 1, number2):
    print(i)
    list_of_numbers.append(i)


print(f"The sum of the numbers between the inputed number is: {sum(list_of_numbers)}")