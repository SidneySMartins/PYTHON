import random
s1 = str(input('Primeiro Aluno: '))
s2 = str(input('Segundo Aluno: '))
s3 = str(input('Terceiro Aluno: '))
s4 = str(input('Quarto Aluno: '))
list = [s1, s2, s3, s4]
student = random.choice(list)
print('Aluno sorteado: {}'.format(student))
