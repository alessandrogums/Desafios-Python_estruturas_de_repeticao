#Faça um programa que calcule o número médio de alunos por turma. 
#Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
#As turmas não podem ter mais de 40 alunos.

turmas=int(input('digite o número de turmas que deseja ter:'))
media=0
for c in range(turmas):
    alunos=int(input('digite a quantidade de alunos por turma:'))
    while not 40>=alunos>0:
        print('o número tem que ser menor do que 40 alunos por turma')
        alunos=int(input('digite a quantidade de alunos por turma:'))
    media+=alunos
print(f'a média de alunos por turma é {int(media/turmas)}')
