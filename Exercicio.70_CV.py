#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

produtos_caros=0
total_gasto=0
lista=[]
contador=0
menor_valor=0
while True:
    nome_produto = str(input('digite o nome do produto:')).strip().lower()
    produto = float(input('digite o valor do produto R$:'))
    while produto<0:
        produto = float(input('digite o valor do produto:'))
    escolha = ' '
    while not escolha in 'SN':
        escolha=str(input('você quer continuar?[S] ou [N]?')).strip().upper()[0]
    if escolha =='N':
        print('estatisticas interrompidas.Saindo do programa...')
        break
#saber a quantidade de produtos acima de 1000 reais
if produto>1000:
    produtos_caros+=1
#calcular o custo total de todos os produtos
total_gasto += produto
saber o nome do produto mais barato
    contador+=1
    if contador==1:
        menor_valor=produto
        lista=[nome_produto]
    elif menor_valor>=produto:
        lista.clear()
        lista.append(nome_produto)
print(f'o total de gasto foi de R${total_gasto:.2f} e tiveram {produtos_caros} produtos acima de 1000 reais')
print(f'o nome do produto mais barato das compras foi:{lista}')
