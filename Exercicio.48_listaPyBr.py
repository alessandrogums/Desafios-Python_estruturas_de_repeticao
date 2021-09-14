# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321


numero=int(input('digite um número:'))
numero_algarismo=numero
qte_algarismo=1
numero_invertido=0
var=0
#usei o número algarismo para saber a quantidade de algarismos deste número, no obj de utilizar o número sem ser reduzido
while not numero_algarismo //10==0:
    qte_algarismo+=1
    numero_algarismo//=10
#calcular o primeiro algarismo #Subtrai 1, já que o primeiro algarismo já conta como 1
primeiro_algarismo=numero//10**(qte_algarismo-1)

while not numero//10 ==0:
    var=numero%10
    numero_invertido+=(var*10**(qte_algarismo-1))
    numero//=10
    qte_algarismo-=1
    var = 0
print(f'o seu número invertido é {numero_invertido+primeiro_algarismo}')
