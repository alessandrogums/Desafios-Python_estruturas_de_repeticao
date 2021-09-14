#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import choice, shuffle


print('-' * 30, 'JOGO DO PAR OU IMPAR', '-' * 30)
resultado = ''
tentativas=0
while True:
    numero = int(input('digite um número de 0 a 10:'))
    escolha = str(input('escolhar Par ou Impar?')).strip().upper()[0]
    # if escolha!='P' and escolha!='I':
    #     print('escolha errada!Precisa ser Par ou Impar')
    #     break
    numero_computador = randint(0, 10)
    escolha_computador = random.choice('PI')
    soma = numero + numero_computador
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'você escolheu {escolha} e o computador {escolha_computador}: a soma deu {soma},ou seja,{resultado}, desse modo: ')
    if escolha == resultado and escolha_computador != resultado:
        print('você ganhou!')
        tentativas+=1
    elif escolha_computador == resultado and escolha!=resultado:
        print('o computador ganhou!')
        break
    elif escolha == escolha_computador:
        print('empate!!')
print(f'Você ganhou {tentativas} vezes do computador!')
print('FIM DO JOGO!')
