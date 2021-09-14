#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior=0
menor=0
for peso in range(1,6):
    peso_pessoa=float(input(f'digite o peso da pessoa nº{peso}'))
    if peso==1:
        maior=peso_pessoa
        menor=peso_pessoa
    else:
        if peso_pessoa>maior:
          maior=peso_pessoa
        elif menor>peso_pessoa :
          menor=peso_pessoa
          
print(f'o maior peso é  {maior:.2f}kg e o menor peso é {menor:.2f}kg')
