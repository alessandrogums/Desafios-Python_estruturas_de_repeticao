# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

n = int(input('digite a quantidade de termos que quer saber:'))
numerador = 1
denominador = 1
contador = 1
denominador_anterior = numerador_anterior = 0
print('a soma dos N termos é:S= 1 + ', end='')
mmc = 1
soma = 0
while n >= contador:
    contador += 1
    numerador += 1
    denominador += 2
    print(f'{numerador}/{denominador}', end=' + ')
# Fazer a soma de maneira separada, já que os n termos serviram só como medida ilustrativa
cont = 1
numerador = 1
denominador = 1
contador = 2
numerador_anterior = denominador_anterior = 0
while n >= cont:
    numerador += 1
    denominador += 2
    # agora, como os denominadores não são iguais, é necessário fazer o mmc deles:
    if cont == 1:
        numerador_anterior = denominador_anterior = 1
    den_var = denominador
    den_antes_var = denominador_anterior
    valor = 0
    fator = 0
    contador = 2
    mmc = 1
    while den_antes_var != 1 or den_var != 1:
        soma = 0
        while den_antes_var % contador == 0 and den_var % contador == 0:
            den_antes_var /= contador
            den_var /= contador
            valor += 1
        while den_antes_var % contador == 0:
            den_antes_var /= contador
            valor += 1
        while den_var % contador == 0:
            den_var /= contador
            valor += 1
        fator = contador ** valor
        mmc *= fator
        valor = 0
        contador += 1
    soma = (mmc / denominador_anterior) * numerador_anterior + (mmc / denominador) * numerador
    numerador_anterior = soma
    denominador_anterior = mmc
    cont += 1
#para simplificar a fração final relativa à soma
div=2
while True:
    while soma % div ==0:
        soma/=div
    div+=1
    if soma == div:
        break
div=2
while True:
    while mmc % div ==0:
        mmc/=div
    div+=1
    if mmc==div:
        break
print(f'\n{int(soma)}/{int(mmc)}')
