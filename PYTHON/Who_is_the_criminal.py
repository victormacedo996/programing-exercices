"""
Make a program that asks a person 5 questions about a crime. The questions are:

     "Did you call the victim?"
     "Were you at the crime scene?"
     "Do you live near the victim?"
     "Should it be for the victim?"
     "Have you worked with the victim?" 
     
The program must ultimately issue a rating on the person's participation in the crime. 
If the person responds positively to 2 questions he should be classified as "Suspect", 
between 3 and 4 as "Accomplice" and 5 as "Assassin". Otherwise, he will be classified as 
"Innocent".
"""

print('Exercice - Who is the criminal?')

def getAnswer(answer):
   while True:
       userAnswer = str(input(answer)).lower()
       if userAnswer != 'y' and userAnswer != 'n':
           print('Use Y for yes and N for no')
       else:
           return userAnswer


question1 = getAnswer ('Did you call the victim? ')
question2 = getAnswer ('Were you at the crime scene? ')
question3 = getAnswer ('Do you live close to the victim? ')
question4 = getAnswer ('Should it be for the victim? ')
question5 = getAnswer ('Did you work with the victim? ')

lis = []

score = 0

lis.append(question1)
lis.append(question2)
lis.append(question3)
lis.append(question4)
lis.append(question5)

for item in lis:
   if item == 'y':
       score = score + 1
   else:
       pass

if score == 2:
   print('SUSPECT')
elif score >= 3 and score <= 4:
   print('ACCOMPLICE')
elif score == 5:
   print ('KILLER')
else:
   print ('INNOCENT')