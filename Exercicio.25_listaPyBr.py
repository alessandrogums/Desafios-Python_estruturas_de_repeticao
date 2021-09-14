#Faça um programa que peça para n pessoas a sua idade, ao final 
#O programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

contador = 0
soma = 0
while True:
    idade = int(input(f'digite a idade da pessoa {contador + 1}:'))
    while not 150 > idade > 0:
        idade = int(input('digite sua idade verdadeira.Você digitou ela errado:'))
    if contador == 0:
        soma = idade
    contador += 1
    if contador != 1:
        soma += idade
    escolha = ' '
    while not escolha in 'SN':
        escolha = str(input('você quer continuar?Digite S para sim e N para não:')).strip().upper()[0]
    if escolha == 'N':
        break
media=soma/contador
print(f'a media das idades vale: {media:.1f}')
if 25>media>0:
    print('Isso quer dizer que a turma é jovem!')
elif 60>media>25:
    print('Isso quer dizer que a turma é adulta!')
else:
    print('Isso quer dizer que a turma é idosa!')
