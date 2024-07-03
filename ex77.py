#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('sacar','arrotar','mecanismo','defender','jogar', 'Dever', 'Livros', 'garrafa')

for palavra in tupla:
    print(f'Na palavra {palavra} temos: ',end= '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(' ',letra.upper(), end= '')
    print('')