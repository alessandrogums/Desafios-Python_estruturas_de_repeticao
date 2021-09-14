#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

 nome=str(input('digite seu nome completo:'))
while len(nome)<4:
    nome=str(input('Seu nome completo precisa ter mais de 3 caracteres.Digite-o novamente:'))
idade=int(input('digite sua idade:'))
while not idade in range(0,151):
    idade=int(input('sua idade precisa ser entre 0 a 150.Digite-a novamente:'))
salario=float(input('digite o valor do seu salário R$:'))
while not salario>0:
    salario=float(input('seu salário precisa ser maior do que zero.Digite-o novamente:'))
sexo=str(input('digite seu sexo:M ou F-->')).strip()[0]
while not sexo in 'mfMF':
    print('digitou seu sexo errado')
    sexo=str(input('qual seu sexo:M ou F-->')).strip()[0]
if sexo=='m' or sexo=='M':
    sexo='Masculino'
else:
    sexo='Feminino'
estado_civil=str('qual seu estado civil:'
                 '\n[s]olteir(o/a)'
                 '\n[c]asado(o/a)'
                 '\n[v]viúv(o/a)'
                 '\n[d]ivorciad(o/a)'
                 'digite>>').strip().lower()[0]
while estado_civil not in 's,c,v,d':
    estado_civil=str(input('digite seu estado civil novamente-[s],[c],[v] ou [d]-->'))
if estado_civil=='s' and sexo=='Masculino':
    estado_civil='solteiro'
elif estado_civil=='s' and sexo=='Feminino':
    estado_civil='solteira'
elif estado_civil=='c' and sexo=='Masculino':
    estado_civil='casado'
elif estado_civil=='c' and sexo=='Feminino':
    estado_civil='casada'
elif estado_civil=='v' and sexo=='Masculino':
    estado_civil='viúvo'
elif estado_civil=='v' and sexo=='Feminino':
    estado_civil='viúva'
elif estado_civil=='d' and sexo=='Masculino':
    estado_civil='divorciado'
else:
    estado_civil='divorciada'
print('FICHA DE CADASTRO'
      f'\nseu nome é {nome}'
      f'\nsua idade é {idade}'
      f'\nseu salário é R${salario:.2f}'
      f'\nseu sexo é {sexo}'
      f'\nseu estado civil é {estado_civil}')

