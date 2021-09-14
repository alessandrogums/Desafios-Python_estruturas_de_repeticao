#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*20,'PROGRESSÃO ARITMÉTICA DE 10 TERMOS','='*20)
termo_1=int(input('digite o primeiro termo'))
razao=int(input('digite a razão'))
n=0
for c in range(0,10):
    n+=1
    termo_n = termo_1 + (n - 1) * razao
    print(f'{termo_n}', end='==>')
print(' fim do programa')
