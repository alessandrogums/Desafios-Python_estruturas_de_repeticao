#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
#Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
#O valor zero deve ser informado pelo operador para indicar o final da compra. 
#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
#Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
...


total=0
troco=0
produtos=[]
while True:
    preco_produto=float(input('digite o preço do protudo:R$'))
    if preco_produto==0:
        break
    produtos.append(preco_produto)
    total += preco_produto
print(f'o total foi de R${total:.2f}')
dinheiro=float(input('quanto você dará em dinheiro?'))
while  not dinheiro>=total:
    print('Seu caloteiro!')
    dinheiro=float(input('Forneça um valor igual ou maior do que o total para efetuar a compra:R$'))
print('='*25)
print('Nota:')
for c in range(len(produtos)):
    print(f'produto {c+1} :R$ {produtos[c]}')
print(f'Preço Total: R${total:.2f}')
print(f'Troco: R$ {(dinheiro - total):.2f}')
print('='*25)
