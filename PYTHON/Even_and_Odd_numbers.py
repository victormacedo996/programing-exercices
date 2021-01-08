"""
Create a program that ask for the user 20 integer numbers and separate then in even and 
odd numbers
"""

def getInteger(integer):
   while True:
       try:
           user_input = int(input(integer))
           return user_input
       except ValueError:
           print('You must enter a integer number')

all_numbers = []
even_numbers = []
odd_numbers = []


while len(all_numbers) < 20:
   number = getInteger('Enter a integer number: ')
   all_numbers.append(number)
   if number % 2 == 0:
       even_numbers.append(number)
   else:
       odd_numbers.append(number)

print('All numbers : ', all_numbers)
print('even numbers: ', even_numbers)
print('odd numbers: ', odd_numbers)
print('\n')