 #Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
  
num=int(input('digite um número '))
numero_divisores=0
x=0 # x é a variável de iteração com número de divisores(contador)
for c in range(1,num+1,1):
    divisao=num % c
    if divisao == 0 :
       numero_divisores+=1
       x=numero_divisores
    else:
       x=numero_divisores
if x>2:
    print(f' o número {num} NÃO é primo,pois tem {x} numeros  divisores')
else:
    print(f' o número {num} é PRIMO')
