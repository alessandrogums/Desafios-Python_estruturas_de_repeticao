
# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

qt_1=qt_2=qt_3=qt_4=qt_5=qt_6=0
total_votos=0
while True:
    opcao=int(input('digite em qual candidato irá votar:'
                    '\n[1]Lula'
                    '\n[2]Boulos'
                    '\n[3]Marina'
                    '\n[4]Meireles'
                    '\n[5]caso queira votar Nulo'
                    '\n[6]caso queira votar em branco'
                    '\n[0]finalização da contagem de votos'
                    '\nsendo assim,escolha>>'))
    if opcao==0:
        break
    else:
        total_votos+=1
        if opcao==1:
            qt_1+=1
        elif opcao==2:
            qt_2+=1
        elif opcao==3:
            qt_3+=1
        elif opcao==4:
            qt_4+=1
        elif opcao==5:
            qt_5+=1
        else:
            qt_6+=1
print(f'dos {total_votos} votos totais: '
      f'\no candidato 1(Lula) recebeu {qt_1} votos'
      f'\no candidato 2(Boulos) recebeu {qt_2} votos'
      f'\no candidato 3(Marina) recebeu {qt_3} votos'
      f'\no candidato 4(Meirelles) recebeu {qt_4} votos'
      f'\nhouveram {qt_5} votos nulos'
      f'\nhouveram {qt_6} votos em branco'
      f'\no percentual de votos nulos:{(qt_5/total_votos)*100:.2f}%'
      f'\no percentual de votos em branco:{(qt_6/total_votos)*100:.2f}%')
