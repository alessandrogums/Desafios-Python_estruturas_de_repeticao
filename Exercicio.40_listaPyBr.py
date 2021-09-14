# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio

maior=menor=0
nome_maior=nome_menor=''
soma_veiculos=0
soma_veiculos_2000=qte_veiculos_2000=0
media=0
for c in range(1,2):

    print(f'CIDADE Nº{c}')
    codigo=str(input('digite o código da cidade:'))
    veiculos=int(input('digite o número de veículos de passeio da cidade:'))
    acidentes=int(input('digite o número de acidentes de trânsito:'))

    if c==1:
        maior=acidentes
        menor=acidentes
        nome_maior=nome_menor=codigo
    if acidentes>maior:
        maior=acidentes
        nome_maior=codigo
    elif menor>acidentes:
        menor=acidentes
        nome_menor=codigo

    soma_veiculos += veiculos

    if veiculos<2000:
        soma_veiculos_2000+=veiculos
        qte_veiculos_2000+=1
        media=soma_veiculos_2000/qte_veiculos_2000
    else:
        media=0
print(f'a cidade com maior número de acidentes de veículos possui o código:{nome_maior}, com {maior} acidentes'
      f'\njá a cidade com menor número de acidentes de veículos possui o código:{nome_menor}, com {menor} acidentes'
      f'\na média de veículos nas cinco cidades = {soma_veiculos/5}'
      f'\na média de veículos nas cidades com menos de 2000 veículos de passeio equivale a {media}')
