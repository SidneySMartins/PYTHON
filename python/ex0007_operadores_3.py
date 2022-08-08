from cmath import sqrt


import math
num = int(input('Informe um valor: '))
print('O dobro de {} é: {}'.format(num, (num*2)))
# print('O triplo de {} é: {}'.format(num, (num*3)))
# print('A raiz quadra de {} é: {}'.format(num, (math.sqrt(num))))
print('O triplo de {} é: {}\nA raiz quadra de {} é: {:.2f}'.format(
    num, (num*3), num, ((num**(1/2)))))
