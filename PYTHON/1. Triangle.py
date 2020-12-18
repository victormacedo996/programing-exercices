""""
Make a Program that asks for the 3 sides of a triangle. The program should inform if the values can be a triangle. Indicate, if the sides form a triangle, if it is: equilateral, isosceles or scalene.

     Tips:
     Three sides form a triangle when the sum of any two sides is greater than the third;
     Equilateral Triangle: three equal sides;
     Isosceles Triangle: any two equal sides;
     Scalene Triangle: three different sides;
    """"

print ('Exercise 1 - triangle sides and classification')
def getFloat(Float):
    while True:
       try:
           userFloat = float(input(Float))
           return userFloat
       except ValueError:
           print('Use only numbers and separete decimals with point')




first_side = getFloat('Enter the first side: ')
second_side = getFloat('Enter the second side: ')
third_side = getFloat('Enter the second side: ')


triangle_sides = []

triangle_sides.append(first_side)
triangle_sides.append(second_side)
triangle_sides.append(third_side)

triangle_sides.sort()

## Conditional created to check if the sides imputed by the user form a triangle, if so what it's classification
if triangle_sides[0] + triangle_sides[1] >= triangle_sides[2]: 
   if triangle_sides[0] == triangle_sides[1] and triangle_sides[1] == triangle_sides[2]:
       print('Equilateral triangle')
   elif triangle_sides[0] == triangle_sides[1] or triangle_sides[0] == triangle_sides[2] or triangle_sides[1] == triangle_sides[2]:
       print('Isosceles triangle')
   else:
       print('Scalene triangle')
else:
   print('Does not form a triangle')