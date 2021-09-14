
# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


from random import randint
palpites=0
num=0
singular='tentativa'
variavel_computador=randint(0,10)
print(variavel_computador)
while num != variavel_computador:
    num=int(input('acerte o número que eu estou pensando, no intervalo de 0 a 10:'))
    palpites+=1
if palpites>1:
    singular+='s'
print(f'voce acertou, seu miserável!pensei exatamente no {num}.Contudo, gastou {palpites} {singular} para adivinhar ')
