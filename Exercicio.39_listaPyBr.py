#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
#Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

maior_altura=0
menor_altura=0
lista_altura=[]
lista_nomes=[]
for c in range(0,10):
    numero_aluno=str(input('digite o seu número:'))
    lista_nomes.append(numero_aluno)
    altura_aluno=float(input('digite sua altura, em :'))
    lista_altura.append(altura_aluno)
print(f'o aluno de código {lista_nomes[lista_altura.index(max(lista_altura))]} possui a maior altura,que é {max(lista_altura)}m')
print(f'o aluno de código {lista_nomes[lista_altura.index(min(lista_altura))]} possui a menor altura, que é {min(lista_altura)}m')
