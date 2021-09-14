#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
#o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
#(atribuir 1 ponto por resposta certa).
#Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

from random import choice

alternativas = ['A', 'B', 'C', 'D', 'E']
gabarito = []
nota = 0
maior_nota=0
menor_nota=0
total_alunos=0
media_alunos=0
for c in range(0, 10):
    esc = choice(alternativas)
    gabarito.append(esc)
print(f'o gabarito>>{gabarito}')
while True:
    total_alunos+=1
    print(f'ALUNO NUMERO {total_alunos}')
    for c in range(1, 11):
        questao = str(input(f'digite a resposta da questão {c}:')).strip().upper()[0]
        while not questao in 'ABCDE':
            print('as alternativas da questão só podem estar entre A a E!')
            questao = str(input(f'digite a  resposta da questão {c} novamente:')).strip().upper()[0]
        if questao == gabarito[c - 1]:
            nota += 1
    if total_alunos==1:
        maior_nota=nota
        menor_nota=nota
    else:
        if nota>=maior_nota:
            maior_nota=nota
        elif menor_nota>nota:
            menor_nota=nota
    print(f'sua nota foi:{nota}')
    pergunta = str(input('outro aluno quer participar do sistema:[S]im ou [N]ao:')).strip().upper()[0]
    while not pergunta in 'SN':
        print('digite S para Sim e N para Não')
        pergunta = str(input('outro aluno quer participar do sistema:[S]im ou [N]ao:')).strip().upper()[0]
    if pergunta == 'N':
        break
    media_alunos += nota
    nota=0
print(f'A maior nota entre os alunos no sistema foi:{maior_nota}'
      f'\nenquanto a menor nota foi de:{menor_nota}'
      f'\ntiveram {total_alunos} aluno(s) que utilizaram o sistema'
      f'\na media dos aluno(s) ficou sendo: {media_alunos/total_alunos}')
