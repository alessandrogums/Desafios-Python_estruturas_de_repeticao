# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador=0
n=0
s=0
while n !=999:
    n = int(input('digite um número'))
    s+=n
    contador+=1
print(f'a soma dos {contador-1} digitados foi de {s-999}')

Maior e menor valor
numero = int(input('digite um numero'))
opcoes = str(input('quer continuar?[S] ou [N]'))[0].strip().upper()
contador = 1
maior_valor=numero
menor_valor=numero
soma=numero
while not opcoes == 'N':
    prox_num = int(input('digite um numero'))
    opcoes = str(input('quer continuar?[S] ou [N]'))[0].strip().upper()
    if prox_num>=maior_valor:
        maior_valor=prox_num
    elif menor_valor>prox_num:
        menor_valor=prox_num
    soma += prox_num
    contador+=1
print(f' a media dos {contador} números é {soma/contador}, o maior dos números é {maior_valor} e o menor é {menor_valor}')
