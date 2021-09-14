# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('digite um valor R$:'))
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
resto = valor%50
if valor % 50 ==0:
    cedulas_50 = valor // 50
elif valor%50!=0:
    cedulas_50=valor//50
    cedulas_20= resto//20
    cedulas_10=resto%20//10
    cedulas_1=(resto%20)%10//1
print(f'o número de cédulas de 50 é {cedulas_50}  '
      f'\no número de cédulas de 20 é {cedulas_20}'
      f'\no número de cédulas de 10 é {cedulas_10} '
      f'\no número de cédulas de 1 é {cedulas_1} ')

#simulador de caixa eletrônico(outro método)
valor=int(input('digite o valor que quer retirar no caixa eletrônico'))
cedula_50=cedula_20=cedula_10=cedula_1=0
debito=0
while valor>=50:
    debito=50
    valor-=debito
    cedula_50+=1
while valor>=20:
    debito=20
    valor-=debito
    cedula_20+=1
while valor>=10:
    debito=10
    valor-=debito
    cedula_10+=1
while valor>=1:
    debito=1
    valor-=debito
    cedula_1+=1
print(f'o valor total de cedulas de 50 reais recebida(s):{cedula_50}'
      f'\no valor total de cedulas de 20 reais recebida(s):{cedula_20}'
      f'\no valor total de cedulas de 10 reais recebida(s):{cedula_10}'
      f'\no valor total de cedulas de 1 reais recebida(s):{cedula_1}')
