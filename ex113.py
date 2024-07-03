
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora 
# a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leianum(msg, tipo):
    if tipo == 'float':
        tipagem = float
    elif tipo == 'int':
        tipagem = int
    while True:
        try:
            num = tipagem(input(msg))
        except:
            print(f'ESCREVA ALGO VÁLIDO!')
            continue
        else:
            break
    return num
            



while True:
    try:
        t = int(input('Insira o tipo de número que quer digita [INT-1/ FLOAT-2]: '))
    except:
        print('Escolha entre 1 ou 2.')
    else:    
        if t == 1:
            t = str('int')
            break
        elif t == 2:
            t = str('float')
            break
        else:
            print('INVÁLIDO!')

r = leianum(f'Insira um número {t}: ', t)
print(f'O número é {r}.')