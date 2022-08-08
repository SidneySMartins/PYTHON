import math


n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
addiction = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
multiplication2 = n1 ** n2
division = n1/n2
division2 = n1//n2
rest = n1 % n2
potentiation = pow(n1, n2)

print('{} + {} = {}'.format(n1, n2, addiction))
print('{} - {} = {}'.format(n1, n2, subtraction))
print('{} * {} = {}'.format(n1, n2, multiplication))
print('{} ** {} = {}'.format(n1, n2, multiplication2))
print('{} / {} = {}'.format(n1, n2, division))
print('{} // {} = {}'.format(n1, n2, division2))
print('{} % {} = {}'.format(n1, n2, rest))

print('{} ^ {} = {}'.format(n1, n2, potentiation))
