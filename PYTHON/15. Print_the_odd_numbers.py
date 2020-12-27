"""
print the odd numbers up to user input
"""

def getInteger (integer):
    while True:
        try:
            user_input = int(input(integer))
            return user_input
        except ValueError:
            print('You must enter a integer number')

interval = getInteger('You want to print odd numbers up to: ')

for i in range (1, interval + 1):
    if i % 2 != 0:
        print(i)
    else:
        pass

