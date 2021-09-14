#Encontrar números primos é uma tarefa difícil.
#Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero=int(input('digite um número inteiro:'))
print('os números primos são:',end=' ')
for c in range(2,numero+1):
   div=1
   qte=0
   while not c + 1 == div:
      if c % div == 0 :
         qte+=1
      div+=1
   if qte<=2:
      print(c,end=',')
print('fim')
