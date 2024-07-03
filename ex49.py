# Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tabuada = int(input('Insira um número em que deseja ter acessoa a sua tabuada: '))
for x in range(0,11):
    print(f'{tabuada} x {x} = {tabuada * x}')
