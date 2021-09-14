#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

nome=str(input('digite seu nome completo')).strip().lower()
nome_completo=nome.split()
s=''.join(nome_completo)
print(f'tenho esses nome:{s}')
v=s[::-1]
if s == v:
    print('é um palindromo')
else:
    print('não é um palindromo')
