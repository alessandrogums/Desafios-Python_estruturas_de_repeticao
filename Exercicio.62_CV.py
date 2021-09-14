#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
  #O programa encerrará quando ele disser que quer mostrar 0 termos.
  
primeiro_termo = int(input('digite o primeiro termo da PA'))
razao = int(input('digite a razão da PA'))
num_termos = 0
sequencia = 0
ultimo_termo = 0
numeros_adicionais=1
print('os dez primeiros da sequência são:', end=' ')
while num_termos < 10:
    sequencia = primeiro_termo
    primeiro_termo += razao
    num_termos += 1
    print(f'{sequencia}', end=' ')
while not numeros_adicionais==0:
        numeros_adicionais=int(input('\nquantos termos você quer postar a mais?'))
        inicio = num_termos - 10
        while not inicio==numeros_adicionais:
            primeira_variavel=sequencia+razao
            sequencia+=razao
            inicio+=1
            print(primeira_variavel,end=' ')
print('final do programa')
