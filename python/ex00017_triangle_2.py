from math import hypot
sideOpposite = float(input('Cateto oposto: '))
rightAngle = float(input('Cateto adjacente: '))
hypotenuse = hypot(sideOpposite, rightAngle)

print('Cateto oposto: {:.2f}\nCateto adjacente: {:.2f}\nhypotenuse: {:.2f}'.format(
    sideOpposite, rightAngle, hypotenuse))
