# print('Start!')
# for i in range(6, 0, -1):
#     print(i)
# for i in range(0, 6, 2):
#     # for i in range(6, 0, -1):
#     # print('corre')
#     print(i)
# print('Fim')

start = int(input('Digite o início: '))
end = int(input('Digite o fim: '))
step = int(input('Passo: '))

if start < end:
    for i in range(start, end+1, step):
        print(i)
elif start > end:
    for i in range(1-end, start, step):
        print(i)
print('FIM!')
