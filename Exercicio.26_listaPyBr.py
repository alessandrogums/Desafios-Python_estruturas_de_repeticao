#Numa eleição existem três candidatos. 
#Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

numero_candidatos=int(input('digite o número total de eleitores:'))
contador=0
votos_cand1=0
votos_cand2=0
votos_cand3=0
while  (numero_candidatos-1)>=contador:
    eleitor=int(input('escolha o candidato 1, 2 ou 3:'))

    while not 3>=eleitor>0:
        eleitor=int(input('digite o número 1,2 ou 3, referente ao número do candidato'))

    if eleitor ==1:
        votos_cand1+=1
    elif eleitor==2:
        votos_cand2+=1
    elif eleitor==3:
        votos_cand3+=1

    numero_candidatos-=1
print(f'o candidato 1 recebeu {votos_cand1} votos'
      f'\no candidato 2 recebeu {votos_cand2} votos'
      f'\no candidato 3 recebeu {votos_cand3} votos')
if votos_cand1>votos_cand2 and votos_cand1>votos_cand3:
    print('logo, o candidato 1 ganhou!')
elif votos_cand2>votos_cand3 and votos_cand2>votos_cand1:
    print('logo, o candidato 2 ganhou!')
elif votos_cand3>votos_cand1 and votos_cand3>votos_cand2:
    print('logo, o candidato 3 ganhou!')
else:
    print('deu empate!')
