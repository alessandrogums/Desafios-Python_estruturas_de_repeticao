#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
#Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

import math
ano_inicial=1996
percentual_aumento=1.5
salario_inicial=float(input('digite seu salário:R$'))
ano_contagem=int(input('digite o ano em que voce quer saber seu salário:'))
tempo=ano_contagem-ano_inicial
for c in range(tempo+1):
    salario_inicial=salario_inicial*((100+percentual_aumento)/100)
    percentual_aumento *= 2
print(f'seu salário será R$ {math.ceil(salario_inicial)}')
