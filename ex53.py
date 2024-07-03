#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.

frase = input('Insira uma frase: ')

#conversão
conv = frase.upper().split()
#junção
juncao = ''.join(conv)
#inversão 
invertido = ''

print(f'Sua frase foi {juncao}.')

for letra in range(len(juncao)-1, -1, -1):
    invertido = invertido + juncao[letra]
print(f'A frase invertida fica {invertido}.')

if invertido == juncao:
    print('A frase é um Palíndromo!')
else:
    print('A frase não é um Palíndromo!')