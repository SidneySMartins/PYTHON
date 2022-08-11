import locale
locale.setlocale(locale.LC_ALL, '')
product = float(input('Informe o preço do produto: '))
discount = product * 0.05
finalPrice = product - discount
print('Preço do produto: {}'.format(locale.currency(product)))
print('Desconto do produto: {}'.format(locale.currency(discount)))
print('Preço final do produto: {}'.format(locale.currency(finalPrice)))
