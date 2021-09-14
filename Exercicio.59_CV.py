
# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


import random
from random import randint

num1 = float(input('digite o primeiro número:'))
num2 = float(input('digite o segundo número:'))
opcoes = int(input('ESCOLHA UMA DAS OPÇÕES:'
                   '\n[1]Somar os dois números '
                   '\n[2]multiplicar os dois números'
                   '\n[3]maior entre esses números '
                   '\n[4]novos números'
                   '\n[5]sair do programa'
                   '\nSendo assim, qual é sua escolha?'))
soma = 0
print('='*60)
while not opcoes == 5:
    if opcoes == 1:
        soma = num1 + num2
        print(f'a soma dos dois números da:{soma}')
    if opcoes == 2:
        print(f'a multiplicacao dos dois números é:{num1 * num2}')
    if opcoes == 3:
        if num1 > num2:
            print(f'o numero maior é:{num1}')
        elif num1 == num2:
            print(f'os dois são iguais!!')
        else:
            print(f'o número {num2} é o maior')
    elif opcoes == 4:
        num1 = int(input('digite agora o primeiro novo número:'))
        num2 = int(input('digite agora o segundo novo número:'))
        print('agora o número 1 equivale à {} e o número 2 equivale à {}'.format(num1,num2))
    opcoes = int(input('digite novamente um número entre 1 a 5, de acordo com as opções acima:'))
print('='*60)
print('FIM do programa!')
