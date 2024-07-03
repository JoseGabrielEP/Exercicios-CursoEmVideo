#Vamos criar um menu em Python, usando modularização.

def menu():
    print('=-'*20)
    print('=-'*6,'MENU PRINCIPAL','=-'*6)
    print('=-'*20)
    print('')
    
    print('-'*40)
    print('''Qual sua Opção? \n1- Ver Pessoas Cadastradas;\n2-Cadastrar nova pessoa;\n3-Sair.''')
    print('-'*40)
    while True:
        try:
            opc = input('Insira aqui sua opção [1, 2 ou 3]: ').strip()[0]
            while opc not in '123':
                opc = input('Opção inexistente! [1, 2 ou 3]: ').strip()[0]
            opc = int(opc)
            return opc
            break
        except:
            print('ERRO! INSIRA UMA OPÇÃO VÁLIDA!')

def leitura_dados(caminho = r"C:\Users\\SEU\\CAMINHO\\BANCODEDADOS.txt"):
    print('=-'*20)
    try:
        with open(caminho, 'r', encoding='utf-8') as dados:
            informações = dados.read()
            return informações
    except:
        print('Erro de leitura da arquivos!')

def alteracao_dados(nome, idade):
    print('=-'*20)
    caminho = r'CC:\Users\\SEU\\CAMINHO\\BANCODEDADOS.txt'
    try:
        with open(caminho, 'a', encoding='utf-8') as dados:
            informações = dados.write(f'\n{nome}: {idade} anos.')
            print('CONTEÚDO ADICIONADO COM SUCESSO!')
    except Exception as erro:
        print(f'Erro ao preencher arquivo por {erro}!')