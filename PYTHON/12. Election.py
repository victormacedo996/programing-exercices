"""
In an election there are three candidates. Make a program that asks for the total 
number of voters. Ask each voter to vote and at the end show the number of votes 
for each candidate.
"""
def getInteger(integer):
   while True:
       try:
           user_input = int(input(integer))
           return user_input
       except ValueError:
           print('You must enter a integer number')

def getCandidate(integer):
   while True:
       try:
           user_input = int(input(integer))
           if user_input != 1 and user_input != 2 and user_input != 3:
               print('You must choose between Candidate1, Candidate2 or Candidate3')
           else:
               return user_input
       except ValueError:
           print('You must enter a integer number')


voters = getInteger('Enter the numbers of voters: ')
candidate1 = 0
candidate2 = 0
candidate3 = 0

while candidate1 + candidate2 + candidate3 < voters:
    vote = getCandidate('Enter the correpondant number of your candidate: ')
    if vote == 1:
        candidate1 += 1
    elif vote == 2:
        candidate2 += 1
    else:
        candidate3 += 1

if candidate1 == 1 or candidate1 == 0:
    print(f"The first candidate recived: {candidate1} vote")
else:
    print(f"The first candidate recived: {candidate1} votes")

if candidate2 == 1 or candidate2 == 0:
    print(f"The second candidate recived: {candidate2} vote")
else:
    print(f"The second candidate recived: {candidate2} votes")

if candidate3 == 1 or candidate3 == 0:
    print(f"The third candidate recived: {candidate3} vote")
else:
    print(f"The third candidate recived: {candidate3} votes")