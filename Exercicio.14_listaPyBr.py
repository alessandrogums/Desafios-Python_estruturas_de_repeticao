#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares=[]
impares=[]
qte_pares=0
qte_impares=0
for c in range(1,11):
    num=int(input(f'digite o nº{c}'))
    if num%2==0:
        pares.append(num)
        qte_pares+=1
    else:
        impares.append(num)
        qte_impares+=1
print(f'dos 10 números digitados : {qte_impares} são ímpares e {qte_pares} são pares'
      f'\n os números ímpares digitados anteriormente são:{impares}'
      f'\n os números pares digitados anteriormente são:{pares} ')
