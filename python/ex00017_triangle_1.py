from math import pow, sqrt
sideOpposite = float(input('Cateto oposto: '))
rightAngle = float(input('Cateto adjacente: '))
hypotenuse = sqrt((pow(sideOpposite, 2) + pow(rightAngle, 2)))

print('Cateto oposto: {:.2f}\nCateto adjacente: {:.2f}\nhypotenuse: {:.2f}'.format(
    sideOpposite, rightAngle, hypotenuse))
