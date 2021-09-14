#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
n = int(input('digite o ultimo termo n da sequência da fibonacci:'))
contador = 0
print('os n números da sequência de fibonacci ficam:',end=' ')
if n==1 :
    print('1')
elif n==2:
    print('1,1')
elif n>=3:
    print(1,1,2,end=' ')
    primeiro_termo = 1
    segundo_termo = 1
    terceiro_termo = 2
    while contador <= n - 4:
        primeiro_termo=segundo_termo
        segundo_termo=terceiro_termo
        terceiro_termo=primeiro_termo+segundo_termo
        contador += 1
        print(terceiro_termo, end=' ')
