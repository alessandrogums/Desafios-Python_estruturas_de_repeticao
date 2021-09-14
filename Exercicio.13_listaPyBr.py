#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
#Não utilize a função de potência da linguagem.

#programa que calcula o cálcula da potência através de uma base
base=float(input('qual é o valor da base:'))
expoente=int(input('qual é o valor do expoente:'))
resultado=1
if expoente==0:
    print('o resultado de qualquer número elevado a zero é ZERO!')
else:
    for c in range(1,expoente+1):
        resultado*=base
    print(f'o valor final é: {resultado}')
