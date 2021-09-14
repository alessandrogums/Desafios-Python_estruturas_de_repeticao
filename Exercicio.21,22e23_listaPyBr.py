#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
#Depois,Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input('digite um número:'))
contador = 1
qte=0
if numero==0 or numero==1:
    print('esse número não é primo!')
else:
    print('os números divisores são:', end='')
    while not (numero+1) == contador:
        if numero % contador == 0:
            qte += 1
            print(contador,end=',')
        contador += 1
    print('fim',end='')
    if qte > 2:
        print('\ncomo o número tem mais de dois divisores, logo este número não é primo!')
    else:
        print('\ncomo esse número só tem dois divisores, este número é primo!')
