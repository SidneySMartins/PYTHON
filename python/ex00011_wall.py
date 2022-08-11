width = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))
area = width * height
paint = area / 2
print('Sua parede tem dimensões de {:.2f} x {:.2f} e sua área é de {:.3f}m².'.format(
    width, height, (area)))
print(
    'Para pintar sua parede, você precisara de {:.3f}l de tinta.'.format(paint))
