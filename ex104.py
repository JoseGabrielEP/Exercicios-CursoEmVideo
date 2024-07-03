# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.
#  Ex: n = leiaInt(‘Digite um n: ‘)

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora 
# a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    try:
        inte = int(input(msg))
    except UnboundLocalError:
        print('VAZIO! TENTE NOVAMENTE')
    else:
        print('INVÁLIDO! TENTE NOVAMENTE')
    finally:
        return inte
        


num = leiaInt('Digite um número: ')
print(f'O número digitado foi {num}')
