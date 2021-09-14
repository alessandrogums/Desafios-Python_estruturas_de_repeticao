#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
#para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
#O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar 
#o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

print('BEM-VINDO À ACADEMIA!')
maior_altura = menor_altura = 0
maior_peso = menor_peso = 0
nome_maior_altura=nome_menor_altura=0
nome_maior_peso=nome_menor_peso=0
contador = 0
media_altura=0
media_peso=0
while True:
    codigo = str(input('digite o seu código da academia:')).strip()

    if codigo =='0':
        break

    contador += 1

    altura = float(input('digite sua altura, em metros:'))

    media_altura+=altura
    if contador == 1:
        maior_altura = altura
        menor_altura = altura
        nome_maior_altura=codigo
        nome_menor_altura=codigo
    else:
        if altura > maior_altura:
            maior_altura = altura
            nome_maior_altura=codigo
        elif menor_altura > altura:
            menor_altura = altura
            nome_menor_altura=codigo

    peso = float(input('digite seu peso, em kg:'))
    media_peso+=peso
    if contador==1:
       menor_peso=peso
       maior_peso=peso
       nome_maior_peso=codigo
       nome_menor_peso=codigo
    else:
       if peso>maior_peso:
           maior_peso=peso
           nome_maior_peso=codigo
       elif menor_peso>peso:
           menor_peso=peso
           nome_menor_peso=codigo

print(f'a maior altura foi de {maior_altura:.2f}m, referente à pessoa de código {nome_maior_altura} '
      f'\na menor altura foi de {menor_altura:.2f}m, referente à pessoa de código {nome_menor_altura} '
      f'\no maior peso foi de {maior_peso:.1f} kg, referente à pessoa de código {nome_maior_peso}'
      f'\no menor peso foi de {menor_peso:.1f} kg, referente à pessoa de código {nome_menor_peso}'
      f'\na média das alturas foi de {media_altura/contador:.2f}m'
      f'\na média dos pesos foi de {media_peso/contador:.2f}kg')
