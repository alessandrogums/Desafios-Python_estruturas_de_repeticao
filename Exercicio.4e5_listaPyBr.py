#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
#com uma taxa de crescimento de 1.5%. 
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

anos=0
Pais_a=80000
Pais_b=200000
while not Pais_a>=Pais_b:
    Pais_a*= 1.03
    Pais_b*= 1.015
    anos += 1
print(f'Foram necessários {anos} anos para o País A com {int(Pais_a)} habitantes  passar o país B, de {int(Pais_b)} habitantes ')
print(f'pois, após 62 anos,o país A tinha 500.032 habitantes, enquanto o País B possuia 503.413 habitantes ')

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
Populacao_1 = int(input('informe a população da cidade 1 :'))
taxa_1 = float(input('digite qual é a taxa anual de crescimento desta cidade 1:'))
Populacao_2 = int(input('informe a população inicial da cidade 2: '))
taxa_2 = float(input('digite qual é a taxa anual de crescimento desta cidade 2:'))
anos = 0
if Populacao_1>Populacao_2 and taxa_1>=taxa_2:
    print('A População da cidade 2 nunca chegará a população da cidade 1')
elif Populacao_2>Populacao_1 and taxa_2>=taxa_1:
    print('A população da cidade 1 nunca chegará a pop. da cidade 2')
elif Populacao_1 > Populacao_2:
    while Populacao_1 >= Populacao_2:
        anos += 1
        Populacao_1 *= (1 + taxa_1 / 100)
        Populacao_2 *= (1 + taxa_2 / 100)
    print(f'São necessários {anos} anos para a População da cidade 2({int(Populacao_2)} hab) passar a cidade 1({int(Populacao_1)}hab)')
elif Populacao_2>Populacao_1:
    while Populacao_2 >= Populacao_1:
        anos += 1
        Populacao_2 *= (1 + taxa_2 / 100)
        Populacao_1 *= (1 + taxa_1 / 100)
    print(f'São necessários {anos} para a População da cidade 1({Populacao_1}hab) passar da população da cidade 2({Populacao_2}hab)')
