# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
n = int(input('Insira um número: '))
lista.append(n)
print('Adicionado na posição 0 da lista.')

for x in range(0,4):
    print('=-'*15)
    n = int(input('Insira um número: '))
    if (x == 0):
        if n < lista[0]:
            lista.insert(0, n)
        elif n > lista[0]:
            lista.append(n)
    elif x == 1:
        if n < lista[0]:
            lista.insert(0, n)
        elif (n > lista[0]) and (n < lista[1]):
            lista.insert(1, n)
        elif n > lista[1]:
            lista.append(n)
    elif x == 2:
        if n < lista[0]:
            lista.insert(0, n)
        elif (n > lista[0]) and (n < lista[1]):
            lista.insert(1, n)
        elif (n > lista[1]) and (n < lista[2]):
            lista.insert(1, n)
        elif n > lista[2]:
            lista.append(n)
    elif x == 3:
        if n < lista[0]:
            lista.insert(0, n)
        elif (n > lista[0]) and (n < lista[1]):
            lista.insert(1, n)
        elif (n > lista[1]) and (n < lista[2]):
            lista.insert(1, n)
        elif (n > lista[2]) and (n < lista[3]):
            lista.insert(2, n)
        elif n > lista[3]:
            lista.append(n)
    elif x == 4:
        if n < lista[0]:
            lista.insert(0, n)
        elif (n > lista[0]) and (n < lista[1]):
            lista.insert(1, n)
        elif (n > lista[1]) and (n < lista[2]):
            lista.insert(1, n)
        elif (n > lista[2]) and (n < lista[3]):
            lista.insert(2, n)
        elif (n > lista[3]) and (n < lista[4]):
            lista.insert(3, n)
        elif n > lista[4]:
            lista.append(n)

print('=-'*15)
print(f'A lista ordenada é {lista}')

#CORRIGIR CORRIGIR CORRIGIR CORRIGIR
