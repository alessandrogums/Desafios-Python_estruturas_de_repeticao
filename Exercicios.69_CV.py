#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

contador=0
maior_idade=0
homem=0
mulher_menor=0

while True:
    print(f'Pessoa nº{contador}')
    idade = int(input('digite sua idade:'))
    sexo=' '
    while not sexo in 'HM':
        sexo = str(input('qual seu sexo[H] ou [M]?')).strip().upper()[0]
    print('='*70)
    escolha=' '
    while not escolha in'SN':
        escolha=str(input('você quer continuar:[S] ou [N]?')).strip().upper()[0]
    print('='*70)
    if escolha == 'N':
        print('encerrando o preenchimento de formulários...')
        break
    contador += 1
    if idade>18:
        maior_idade+=1
    if sexo=='H':
        homem+=1
    if  sexo=='M' and idade<20:
        mulher_menor+=1
print(f' do total de {contador} pessoas cadastradas:'
      f'\n{maior_idade} são maiores de idade'
      f'\n{homem} são homens'
      f'\n{mulher_menor} são mulheres menores do que 20 anos')
