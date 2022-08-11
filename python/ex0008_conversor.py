meters = float(input('Informe um valor: '))
km = meters / 1000
hm = meters / 100
dam = meters / 10
dm = meters * 10
cm = meters * 100
mm = meters / 1000

print('Medida informada: {:.2f}\nKm: {:.2f}\nHm: {:.2f}\nDm:{}\nM: {:.2f}\nDm: {:.2f}\nCm: {:.2f}\nMm: {:.2f}'.format(
    meters, km, hm, dam, meters, dm, cm, mm))
