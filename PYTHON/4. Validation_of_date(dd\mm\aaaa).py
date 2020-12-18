"""
Make a Program that asks for a date in the format dd / mm / yyyy and determine if it is a valid date.
"""
print('Exercice - Formated date dd/mm/aaaa')

from datetime import datetime, date
date_input = input('Date (dd/mm/yyyy): ')
try:
   valid_date = datetime.strptime(date_input, '%d/%m/%Y').date()
   print('sucssess')
except ValueError:
   print('Invalid date!')