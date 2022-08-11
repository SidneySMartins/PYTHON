num = int(input('Digite um número: '))
print('A tabuada de {}:'.format(num))
for index in range(1, 11):
    print('{} X {} = {}'.format(num, index, (num*index)))
