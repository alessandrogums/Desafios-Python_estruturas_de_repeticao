#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num=int(input('digite um número qualquer: '))
fatorial=0
produto=1
primeiro_termo=num
print(f'o fatorial de {primeiro_termo}!=',end=' ')
while not num==1:
   print(f'x{num} ', end=' ')
   produto*=num
   num-=1
print(f' = {produto}', end=' ')
