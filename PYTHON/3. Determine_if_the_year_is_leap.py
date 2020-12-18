""""
Make a Program that asks for a number corresponding to a certain year and then inform if this year is leap or not.
"""
print('Exercice - Determine if the year is a leap year')

def getInteger(integer):
   while True:
       try:
           userInt = int(input(integer))
           return userInt
       except ValueError:
           print('You must enter an integer')

year = getInteger('Enter a year: ')

if year % 4 == 0:
   if year % 100 == 0:
       if year % 400 == 0:
           print('leap year')
       else:
           print('not a leap year')
   else:
       print('leap year')
else:
   print('not a leap year')