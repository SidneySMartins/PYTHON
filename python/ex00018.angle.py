from math import cos, sin, tan, radians

angle = float(input('Informe o valor do ângulo: '))

print('Ângulo: {:.1f}º\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(
    angle, sin(radians(angle)), cos(radians(angle)), tan(radians(angle))))
