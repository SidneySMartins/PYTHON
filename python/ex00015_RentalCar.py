import locale
days = float(input('Quantidade de dias alugados: '))
km = float(input('Total de Quilômetros(km) rodados: '))
locale.setlocale(locale.LC_MONETARY, '')
pricePerDay = days * 60
pricePer_km = km * 0.15
finalPrice = pricePerDay + pricePer_km
print('Total de dias alugados: {}.\nKm percorridos: {:.2f}'.format(days, km))
print('Valor a pagar: {}'.format(locale.currency(pricePerDay)))
print('Valor a pagar: {}'.format(locale.currency(pricePer_km)))
print('Valor a pagar: {}'.format(locale.currency(finalPrice)))
