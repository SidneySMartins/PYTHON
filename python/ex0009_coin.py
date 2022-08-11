import babel.numbers
import locale
locale.setlocale(locale.LC_ALL, '')
money = float(input('Total de Dinheiro (Real): '))
dollar = money/5.07
print('Total na Carteira: {}'.format(locale.currency(money)))
print('Total em Dólares: ', babel.numbers.format_currency(
    dollar, 'USD', locale='en_US'))
