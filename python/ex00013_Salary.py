import locale
from operator import ne
locale.setlocale(locale.LC_ALL, '')
salary = float(input('Informe o novo salário: '))
increment = salary * 0.15
newSalary = salary + increment
print('Salário Atual: {}.'.format(locale.currency(salary)))
print('Aumento de 15%: {}.'.format(locale.currency(increment)))
print('Novo Salário: {}.'.format(locale.currency(newSalary)))
