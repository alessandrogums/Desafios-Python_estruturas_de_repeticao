#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1=int(input('digite o valor do primeiro número inteiro:'))
num2=int(input('digite o valor do segundo número inteiro:'))
if num2>num1:
    print('os números entre o número 1 e o número 2  são:')
    for c in range(num1+1,num2):
        print(c,end=' ')
else:
    print('os números entre o número 2 e o número 1 são:')
    for c in range(num2+1,num1):
        print(c,end=' ')
 
#Altere o programa anterior para mostrar no final a soma dos números.

 num1 = int(input('digite o primeiro número inteiro:'))
num2 = int(input('digite o segundo número inteiro:'))
soma = 0
if num2 > num1:
    for c in range(num1 + 1, num2):
        soma += c
    print(f'a soma dos números inteiros entre o {num1} e o {num2} equivale a {soma}')
else:
    for c in range(num2 + 1, num1):
        soma += c
    print(f'a soma dos números inteiros entre o {num2} e o {num1} equivale a {soma}')
