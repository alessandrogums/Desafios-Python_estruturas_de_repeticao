# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos 
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
# Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
# O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

nome=' '
lista_atletas=[]
lista_saltos=[]
media_saltos=0
lista_media=[]

while True:
    nome=str(input('digite o nome do atleta:')).strip().upper()
    if nome =='':
        break
    else:
        lista_atletas.append(nome)
        for c in range(1,6):
            salto=float(input(f'digite o salto nº{c},em m:'))
            lista_saltos.append(salto)
        print('--------RESULTADO---------------------')
        print(f'o resultado do atleta {nome} :'
              f'\nmelhor salto:{max(lista_saltos)}m'
              f'\npior salto:{min(lista_saltos)}m')
        lista_saltos.remove(max(lista_saltos)), lista_saltos.remove(min(lista_saltos))
        media_saltos=(sum(lista_saltos)/len(lista_saltos))
        print(f'a media de saltos foi de:{media_saltos:.1f}m')
        lista_media.append((media_saltos))
        lista_saltos.clear()
        print('-------------------------------------')

print('Atleta        média de saltos')
for c in range(0,len(lista_atletas)):
    print(lista_atletas[c],end='  ')
    print(f'{lista_media[c]:.1f}')

melhor_media=lista_media.index(max(lista_media))

print('=-'*30)
print(f'O CAMPEÃO FOI >>>>>{lista_atletas[melhor_media]}')
print('=-'*30)
