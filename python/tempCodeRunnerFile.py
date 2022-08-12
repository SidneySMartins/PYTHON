start = int(input('Digite o início: '))
end = int(input('Digite o fim: '))
step = int(input('Passo: '))

if start < end:
    for i in range(start, end+1, step):
        print(i)
elif start > end:
    for i in range(end, start, step):
        print(i)
print('FIM!')