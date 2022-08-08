print('Welcome!')
g = input("Guess number (Escola um número): ")
guess = int(g)


if guess == 5:
    print('Você venceu! (You win!)')
else:
    if guess <= 5:
        print('Muito baixo (Too low)')
    else:
        print('Too High')

print('Game over!')
