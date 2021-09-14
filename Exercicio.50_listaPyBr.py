# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
#Faça um programa que calcule o valor de H com N termos.


n =  int(input("Digite o número de termos que desejas:"))
soma= 0
denominador=2
if n==1:
    print('os n termos são: 1', end='')
else:
    print('os n termos são: 1 +', end=' ')
    for c in range(2,n+1):
        print(f'1/{denominador}',end=' ')
        print(' + ' if n>c else ' = ',end='')
        denominador+=1
for c in range(1,n+1):
       soma = soma + 1/c
print(f'{soma:.2f}')
