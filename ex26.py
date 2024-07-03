#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = (input("Escreva uma frase qualquer: \n").upper()).strip()
contagem_A = frase.count('A')
loc1 = frase.find('A')
loc2 = frase.rfind('A')

print(f'Na frase inserida existem {contagem_A} letras "A"')
print('-' * 30)
print(f'O primeiro "A" da frase está na posição {loc1}.')
print('-' * 30)
print(f'O último "A" da frase está na posição {loc2}.')