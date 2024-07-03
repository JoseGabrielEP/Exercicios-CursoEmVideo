def ajuda(comando):
    """Este é um programa feito para testar as docstrings.
    O único objetivo é estudar.
    """
    help(comando)

while True:
    opcao = input('Insira a biblioteca ou comando que deseja ver [FIM para encerrar]: ').strip()
    if opcao.upper() == 'FIM':
        break
    else:
        ajuda(opcao)
        