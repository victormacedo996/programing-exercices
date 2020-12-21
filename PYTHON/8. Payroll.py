"""
Make a program for the calculation of a payroll, knowing that the discounts are from the 
Income Tax, which depends on the gross salary (according to the table below) and 3% for the 
Union and that the FGTS (tax) corresponds to 11% of the Gross Salary, but it is not discounted 
(it is the company that deposits). The Net Salary corresponds to the Gross Salary less 
discounts. The program should ask the user for the value of their hour and the number of 
hours worked in the month.

     IR discount:
     Gross salary up to 900 (inclusive) - exempt
     Gross Salary up to 1500 (inclusive) - 5% discount
     Gross Salary up to 2500 (inclusive) - 10% discount
     Gross Salary above 2500 - 20% discount 
     
Print the information on the screen, arranged according to the example below. 
In the example, the hour value is 5 and the hour amount is 220.
"""
def getFloat(Float):
    while True:
       try:
           userFloat = float(input(Float))
           return userFloat
       except ValueError:
           print('Use only numbers and separete decimals with point')

def getInteger(integer):
   while True:
       try:
           userInt = int(input(integer))
           return userInt
       except ValueError:
           print('You must enter an integer')

def incomeTaxTax(salary): ## Function to get the tax of the income tax according to the salary
    if salary <= 900:
        tax = 0
    elif salary > 900 and salary <= 1500:
        tax = 5
    elif salary > 1500 and salary < 2500:
        tax = 10
    elif salary > 2500:
        tax = 20
    return tax

def incomeTax (salary, tax):
    if salary <= 900:
        pass
    elif salary > 900 and salary <= 1500:
        salary = salary * tax / 100
    elif salary > 1500 and salary < 2500:
        salary = salary * tax / 100
    elif salary > 2500:
        salary = salary * tax / 100

    return salary

def FGTS(salary): ## Brazilian tax 
    FGTS = salary * 0.11
    return FGTS

def INSS(Salary): ## Brazilian tax
    INSS = salary * INSS_tax / 100
    return INSS

def syndicate(salary):
    syndicate = salary * 0.03
    return syndicate


## Getting inputs
value_per_hour = getFloat('How much working hour of the employee? ')
hours = getInteger ('For haw many hours do he/she works? ')
INSS_tax = getFloat(f"How many % is the INSS tax? ")

## Making the calculations with the inputs
salary = value_per_hour * hours
income_tax_tax = incomeTaxTax(salary)
income_tax = incomeTax(salary, income_tax_tax)
FGTS = FGTS(salary)
syndicate = syndicate(salary)
INSS = INSS(salary)
liquid_salary = salary - income_tax - INSS - syndicate

## Final print
print(f"Brute salary: ({hours} * {value_per_hour})                  : R${salary}")
print(f"(-) Income tax ({income_tax_tax}%)                        : R${income_tax}")
print(f"(-) INSS ({INSS_tax}%)                             : R${INSS}")
print(f"(-) Syndicate (3%)                          : R${syndicate}")
print(f"FGTS (11%)                                  : R${FGTS}")
print(f"Liquid salary                               : R${liquid_salary}")






