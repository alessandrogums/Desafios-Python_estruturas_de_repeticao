#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas
#, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

media=0
qte_termos=0
temperaturas=[]
while True:
    temperatura=float(input('digite uma Temperatura(ºC ):'))
    qte_termos+=1
    temperaturas.append(temperatura)
    escolha=' '
    while not escolha in 'SN':
        escolha=str(input('Você quer continuar-[S] ou [N]:')).strip().upper()[0]
    if escolha =='N':
        break
print(f'a média das {len(temperaturas)} temperaturas foi {sum(temperaturas)/len(temperaturas)}ºC')
print(f'sendo a maior temperatura de {max(temperaturas)}ºC e a mínima de {min(temperaturas)} ')
