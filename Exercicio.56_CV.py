# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


soma_idades=0
media_idades=0
idade_homem=0
qte_mulher=0
lista_homens=[]
lista_mulheres=[]

for pessoa in range(1,6):
    nome=str(input(f'digite o nome completo da pessoa nº{pessoa}:'))
    idade=int(input(f'digite a idade da idade da pessoa nº {pessoa}:'))
    sexo=str(input(f'digite o sexo da pessoa nº{pessoa}(M ou H): ')).strip().upper()
    soma_idades+=idade
    media_idades=int((soma_idades)/pessoa)
    if sexo=='H':
        # lista_homens.append(nome)
        if idade>=idade_homem:
            idade_homem=idade
            lista_homens=(nome)
    else:
       if idade<20:
           qte_mulher+=1
print('a média da idade de todos os indivíduos é de {} anos'.format(media_idades))
print(f'o homem com a maior idade é {lista_homens}, com a idade de {idade_homem} anos')
print(f'existem {qte_mulher} mulheres com menos de 20 anos ')
