"""
The Fibonacci series is formed by the sequence 1,1,2,3,5,8,13,21,34,55, ... 
Make a program capable of generating the series up to the nth term.
"""

def fibonacci (number_of_terms):
   sequence = [0, 1]
   i = 0
   while number_of_terms >= len(sequence):
       fibonacci = sequence[i] + sequence[i + 1]
       sequence.append(fibonacci)
       i = i + 1
   return sequence
   
def getInteger(integer):
   while True:
       try:
           userInteger = int(input(integer))
           return userInteger
       except ValueError:
           print('You must enter with a integer number')

terms = getInteger('How many term do you want with fibonacci sequence? ')
fibonacci_sequence = fibonacci(terms)
print(*fibonacci_sequence, sep = ', ')