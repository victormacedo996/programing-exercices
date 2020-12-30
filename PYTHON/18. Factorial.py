"""
Make a program that calculate the factorial of a integer inputed number
"""

def getInteger(integer):
   while True:
       try:
           userInteger = int(input(integer))
           return userInteger
       except ValueError:
           print('You must enter with a integer number')

number = getInteger('Enter a integer number: ')
result = 1
for item in range(1, number + 1):
   result = result * item

print(result)