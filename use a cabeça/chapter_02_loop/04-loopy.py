from random import randint
secret = randint(1, 10)
number = 0
while number != secret:
    answer = input("Adivinhe o número: ")
    number = int(answer)
    if number == secret:
        print('Parabéns você venceu!')
    elif number > secret:
        print('Valor Muito alto!')
    else:
        print('Valor muito baixo!')

print('Fim de jogo')
