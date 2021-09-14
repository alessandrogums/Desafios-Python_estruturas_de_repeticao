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
