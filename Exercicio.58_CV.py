#O computador vai "pensar" em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

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
