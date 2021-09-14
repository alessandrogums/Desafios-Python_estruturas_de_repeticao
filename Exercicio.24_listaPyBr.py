#Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
contador = 0
while True:
    nota = float(input('digite uma nota:'))
    while not 10 >= nota > 0:
        nota = float(input('digite uma nota entre 0 e 10!:'))
    contador+=1
    if contador==1:
        soma=nota
    else:
        soma+=nota
    escolha = ' '
    while not escolha in 'S,N':
        escolha = str(input('você quer continuar adicionando notas?Digite S para sim e N para não:')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'a média dos {contador} números digitados é: {soma / contador:.1f}')
