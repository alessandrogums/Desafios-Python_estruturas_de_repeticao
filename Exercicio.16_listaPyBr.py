#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.


primeiro_termo=0
segundo_termo=1
terceiro_termo=primeiro_termo+segundo_termo
print(f'{primeiro_termo} {segundo_termo} {terceiro_termo}',end=' ')
while terceiro_termo<=500:
    primeiro_termo=segundo_termo
    segundo_termo=terceiro_termo
    terceiro_termo=segundo_termo+primeiro_termo
    print(terceiro_termo,end=' ')
