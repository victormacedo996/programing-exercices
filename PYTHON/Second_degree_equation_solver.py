""""
Make a program that calculates the square roots of a second degree equation, in the form ax2 + bx + c. 
The program should ask for the values of a, b and c and make the consistencies, informing the user in the 
following situations:

     If the user reports the value of A equal to zero, the equation is not of the second degree and the program should not ask for the other values, being closed;
     If the calculated delta is negative, the equation has no real square roots. Inform the user and close the program;
     If the calculated delta is equal to zero, the equation has only one real root; inform the user;
     If the delta is positive, the equation has two real roots; inform the user;
""""
print('Exercice - Second degree equation (ax^2 + bx + c)'


def getFloat(Float):
   while True:
       try:
           userFloat = float(input(Float))
           return userFloat
       except ValueError:
           print('Use only numbers and separete decimals with point')

a = getFloat('Enter a value: ')
if a == 0:
   print('This is not a second degree equation')
else:
   b = getFloat('Enter b value: ')
   c = getFloat('Enter c value: ')

   import math
   
   try:
       delta = math.sqrt(((b**2) - (4 * a * c)))
       breaker = False
   except ValueError:
       breaker = True
       print('The equation has no real roots')
   else:
       if breaker == True:
           pass
       elif delta == 0:
           result = ((b * (-1)) + delta)/(2 * a)
           print(result)
       else:
           result1 = ((b * (-1)) + delta)/(2 * a)
           result2 = ((b * (-1)) - delta)/(2 * a)
           print(result1)
           print(result2)
