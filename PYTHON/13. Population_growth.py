"""
Make a program that asks the population of two countries and their annual population 
growth rates and inform the user how long it will take for the first country to reach 
the population of the second
"""

def getGrowTax(Float):
    while True:
        try:
            GrowTax = float(input(Float))
            return GrowTax
        except ValueError:
            print('Use only numbers and separete decimals with point')

def getPopulation(integer):
    while True:
        try:
            population = int(input(integer))
            if population <= 0:
                print('Someone must live in the country')
            else:
                return population
        except ValueError:
            print('You must enter an integer')

def getAnswer(answer):
    while True:
        userAnswer = str(input(answer)).lower()
        if userAnswer != 'y' and userAnswer != 'n':
            print('Use Y for yes and N for no')
        else:
            return userAnswer

def years (pop_pais_A, pop_pais_B, growth_tax_A, growth_tax_B):
    anos = 0
    while pop_pais_A <= pop_pais_B:
        pop_pais_A = pop_pais_A * growth_tax_A
        pop_pais_B = pop_pais_B * growth_tax_B
        anos = anos + 1
    print('Demorará ' + str(anos) + ' anos para a população do país A se igualar a do país B')

loop = 'y'
while loop == 'y':
    pop_pais_A = getPopulation('How many people live in the Country A? ')
    pop_pais_B = getPopulation('How many people live in the Country B? ')
    growth_tax_A = getGrowTax('What is the growth tax of country A? ')
    growth_tax_B = getGrowTax('What is the growth tax of country B? ')

    if growth_tax_A < growth_tax_B:
        print('This will never work...')
        loop = getAnswer('Do you want to make another consult? (Y/N) ')
    else:
        years(pop_pais_A, pop_pais_B, growth_tax_A, growth_tax_B)
        loop = getAnswer('Do you want to make another consult? (Y/N) ')