# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
n = int(input('Insira um número: '))
pergunta = input('Quer continuar: [Sim / Não] \n').title().strip()[0]
lista.append(n)

while True:
    print('=-'*15)
    if pergunta in 'S':
        n = int(input('Insira um número: '))
        pergunta = input('Quer continuar: [Sim / Não] \n').title().strip()[0]
        if n not in lista:
            lista.append(n)
    elif pergunta in 'N':
        break
    else:
        pergunta = input('Houve um erro. Quer continuar: [Sim / Não] \n').title().strip()[0]
lista.sort()
print(f'A lista inteira ficou em ordem crescente: {lista}')