#O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
#Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
#Considere que o cliente deve informar quando o pedido deve ser encerrado.

print('         Lanchonete-Tabela de preços'
      '\nEspecificação          código       preço'
      '\ncachorro-quente        100          R$1,20'
      '\nBauru simples          101          R$1,30'
      '\nBauru com Ovo          102          R$1,50'
      '\nHamburguer             103          R$1,20'
      '\nCheeseburguer          104          R$1,30'
      '\nRefri                  105          R$1,00')

lista_codigos=[]
for c in range(100, 106):
    lista_codigos.append(c)
lista_precos=[1.20,1.30,1.50,1.20,1.30,1]
total=0
compras=[]
valores_produto=[]
quant=[]
while True:
    codigo=int(input('digite o código do produtor que você irá querer(de 100 a 105):'))
    while codigo>105 or codigo<100:
        codigo=int(input('digitou um valor fora do intervalo.Digite o código do produto que irá querer, sendo entre 100 a 105:'))
    compras.append(codigo)
    preco=lista_precos[lista_codigos.index(codigo)]
    valores_produto.append(preco)
    print(f'o preço do produto é R$ {preco}')

    quantidade=int(input('digite a quantidade do produto que você irá querer:'))
    quant.append(quantidade)
    total+=preco*quantidade
    escolha=' '
    while not escolha in 'SN':
        escolha=str(input('Você quer continuar comprando mais dos nossos produtos?digite [S]im ou [N]ão:')).strip().upper()[0]
    if escolha=='N':
        print('okay, então tudo ficou :')
        print('='*30)
        print('código dos produtos:')
        for c in range(0, len(compras)):#len(compras)==len(valores_produto)
            print(compras[c])
        print('preço dos produtos:')
        for c in range(0,len(valores_produto)):
            print(valores_produto[c])
        print('quantidade de cada produto:')
        for c in range(0, len(quant)):
            print(quant[c])
        print('='*30)
        print(f'total:R${total}')
        print('='*30)
        break
