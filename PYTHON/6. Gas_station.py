"""
A gas station is selling fuel with the following discount table:

     Alcohol:
        up to 20 liters, 3% discount per liter
        over 20 liters, 5% discount per liter
     Gasoline:
        up to 20 liters, 4% discount per liter
        above 20 liters, discount of 6% per liter 

Write an algorithm that reads the number of liters sold, the type of fuel 
(coded as follows: A-alcohol, G-gasoline), calculate and print the amount to be 
paid by customer knowing that the price of a liter of gasoline is $2.50 the price of a 
liter of alcohol is $1.90.

"""

print('Exercice - gas station descount')

def getFloat(Float):
   while True:
       try:
           userFloat = float(input(Float))
           return userFloat
       except ValueError:
           print('Use only numbers and separete decimals with point')

def getFuel(fuel):
   while True:
       userFuel = str(input(fuel)).lower()
       if userFuel != 'a' and userFuel != 'g':
           print('Use A for alcohool or G for gasoline')
       else:
           return userFuel

fuel_type = getFuel('Do you want alcohool or gasoline? ')
liters = getFloat('How many liters do you want? ')

if fuel_type == 'a':
   if liters <= 20:
       descount = (liters * 1.9) * 0.97
       print(f"You are paying ${descount}")
   elif liters > 20:
       descount = (liters * 1.9) * 0.95
       print(f"You are paying ${descount}")
else:
   if liters <= 20:
       descount = (liters * 2.5) * 0.96
       print(f"You are paying ${descount}")
   elif liters > 20:
       descount = (liters * 2.5) * 0.94
       print(f"You are paying ${descount}")

print('\n')