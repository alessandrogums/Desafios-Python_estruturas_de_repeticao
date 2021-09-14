#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n=int(input('com quantos números você pretende trabalhar:'))
contador=0
maior=0
menor=0
soma=0
while not contador>=n:
    num=float(input(f'digite o número nº{contador+1}'))
    soma+=num
    contador+=1
    if contador==1:
       maior=num
       menor=num
    elif contador>1:
            if num>=maior:
                maior=num
            elif menor>num:
                menor=num
print(menor,maior,soma)

#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n=int(input('com quantos números você pretende trabalhar:'))
contador=0
maior=0
menor=0
soma=0
while not contador>=n:
    num=float(input(f'digite o número nº{contador+1},precisando ser entre 0 e 1000'))
    while not 1000>=num>=0:
        num=float(input(f'digite o númeroº{contador+1} novamente:'))
    soma+=num
    contador+=1
    if contador==1:
       maior=num
       menor=num
    elif contador>1:
            if num>=maior:
                maior=num
            elif menor>num:
                menor=num
print(menor,maior,soma)
