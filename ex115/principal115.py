from funções import menu, leitura_dados, alteracao_dados
from time import sleep

while True:
    opcao = menu()
    if opcao == 1:
        print('LOADING...')
        sleep(1)
        dados = leitura_dados()
        print(dados)
        print('=-'*20)
        try:
            retorno = input('Voltar ao começo do programa? [S/N]: ').strip().upper()[0]
            if retorno in 'S':
                continue
            elif retorno in 'N':
                break
            else:
                retorno = input('OPÇÃO INVÁLIDA! Voltar ao começo do programa? [S/N]: ').strip().upper()[0]
        except:
            print('ERRO! PERGUNTANDO NOVAMENTE...')
    if opcao == 2:
        try: 
            name = input('Insira o nome da pessoa cadastrada: ').strip().title()
            howold = int(input('Insira a idade da pessoa cadastrada: '))
            print('Adicionando ao banco de dados...')
            sleep(1)
            modificacao = alteracao_dados(name, howold)
            modificado = leitura_dados()
            print(modificado)
            print('=-'*20)
            try:
                retorno = input('Voltar ao começo do programa? [S/N]: ').strip().upper()[0]
                if retorno in 'S':
                    continue
                elif retorno in 'N':
                    break
                else:
                    retorno = input('OPÇÃO INVÁLIDA! Voltar ao começo do programa? [S/N]: ').strip().upper()[0]
            except:
                print('ERRO!')
        except Exception as erro:
            print(f'Erro na nova entrada de dados devido à {erro}')
    if opcao == 3:
        print('Encerrando programa...')
        sleep(1)
        break

print('PROGRAMA ENCERRADO!')