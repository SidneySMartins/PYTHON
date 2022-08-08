number = input('Guess the number: ')
guess = int(number)

if guess == 3:
    print('Valor informado é muito baixo!')
elif guess == 5:
    print('Você ganhou!')
elif guess > 5:
    print('Valor informado é muito alto!')
elif guess > 10:
    print('Você perdeu!')
print('Game over!')
