#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

N=int(input('digite o número de termos para serem visualizados:'))
p=0
s=1
t=s+p
contador=0
print(f' a sequência de fibonacci fica:{p}>{s} ' ,end=' ')
while contador<=N-3:
    t=p+s
    p=s
    s=t
    contador+=1
    print(f'>{t}',end=' ')
