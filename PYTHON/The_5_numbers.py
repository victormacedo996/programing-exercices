"""
Make a program that reads 5 numbers and reports the largest number and the mean of 
these numbers
"""
def getFloat(Float):
    while True:
        try:
            number = float(input(Float))
            return number
        except ValueError:
            print('Use only numbers and separete decimals with point')

def getInteger(integer):
    while True:
        try:
            user_input = int(input(integer))
            return user_input
        except ValueError:
            print('You must enter a integer number')

def numberLists (number_of_items, list_of_numbers):
    for i in range(1, number_of_items + 1):
        if i == 1:
            i = '1st'
        elif i == 2:
            i = '2nd'
        elif i == 3:
            i = '3rd'
        else:
            i = f"{i}th"

        number = getFloat(f"Enter the {i} number: ")
        list_of_numbers.append(number)

list_of_numbers = []

number_of_items = getInteger ('Enter how many numbers do you want to use: ')
numberLists (number_of_items, list_of_numbers)

list_of_numbers.sort()
print(f"The largest number is: {list_of_numbers[-1]}")

mean = sum(list_of_numbers) / len(list_of_numbers)

print(f"The sum of the numbers is {sum(list_of_numbers)}")
print(f"The mean of the numbers is {mean}")