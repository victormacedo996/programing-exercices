"""
Make a program that asks for two numbers, base and exponent, calculate and show the 
first number raised to the second number. Do not use the language power function.
"""

def getInteger(integer):
    while True:
        try:
            userInput = int(input(integer))
            return userInput
        except ValueError:
            print("Enter a integer number")

def potency (base, exponent):
    if exponent == 1:
        return base
    elif exponent == -1:
        return -base
    else:
        if exponent > 1:
            potency = base * base
            exponent -= 3
            while exponent >= 0:
                potency = potency * base
                exponent -= 1
            return potency
        else:
            potency = base * base
            exponent += 2
            while exponent < 0:
                potency = potency * base
                exponent += 1
            potency = 1 / potency
            return potency

base = getInteger ('Enter a number to be the base number: ')
exponent = getInteger ('Enter a number to be the exponent number: ')
print(potency(base, exponent))

