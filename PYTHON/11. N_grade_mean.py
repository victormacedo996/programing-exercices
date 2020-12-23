"""
Make a program that asks for an undetermined 
amount of grades and at the end I return the average of those grades

"""

def getFloat(Float):
   while True:
       try:
           user_input = float(input(Float))
           if user_input < 0 or user_input > 10:
               print('Enter a grade between 0 and 10')
           else:
               return user_input
       except ValueError:
           print('Use only numbers and separede decimals with point')

def getAnswer(answer):
   while True:
       user_input = str(input(answer)).lower()
       if user_input != 'y' and user_input != 'n':
           print('Use only Y for yes and N for no')
       else:
           return user_input
           

i = 1
grade_list = []
resume = 'y'
while resume == 'y':
   if i == 1:
       r = f"{i}st"
   elif i == 2:
       r = f"{i}nd"
   elif i == 3:
       r = f"{i}rd"
   else:
       r = f"{i}th"
   grade = getFloat(f"Enter {r} grade: ")
   grade_list.append(grade)
   resume = getAnswer('Do you want to add another grade? ')
   i = i + 1

mean = sum(grade_list) / len(grade_list)

print(f"The mean of the students grade is: {mean}")
