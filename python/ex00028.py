from random import randint
from time import sleep
computer = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if(player == computer):
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI!, Eu pensei no número {} e não no {}!'.format(computer, player))
