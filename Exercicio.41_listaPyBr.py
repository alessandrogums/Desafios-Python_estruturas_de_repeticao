# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


print(f"{('INFORMAÇÕES DE DÍVIDA'):^60}")
print('Quantidade de parcelas      %juros sobre o valor inicial da dívida'
      '\n1                                  0'
      '\n3                                  10'
      '\n6                                  15'
      '\n9                                  20'
      '\n12                                 25')
while True:
    juros=0
    contador=1
    divida = float(input('digite o valor da sua dívida:'))

    if divida==0:
        break

    parcelas = int(input('digite a quantidade de vezes que você quer parcelar'))
    while not 12>=parcelas>=0:
        parcelas=int(input('As parcelas precisam ser menores do que 12 e maiores do que zero.Então, digite novamente a quantidade:'))
    if parcelas //3 ==0:
        juros=0
    elif parcelas//3==1:
        juros=10
    else:
        juros=10
        while not parcelas//3 ==contador:
            juros+=5
            contador+=1
    print('=-'*15)
    print(f'Valor da Dívida=R${divida+divida*juros/100:.2f}'
          f'\nValor dos Juros=R${divida*juros/100:.2f}'
          f'\nQuantidade de parcelas={parcelas}'
          f'\nValor da parcela=R${(divida+divida*juros/100)/parcelas:.2f}')
    print('=-'*15)
print('Você pagou sua dívida então!')
