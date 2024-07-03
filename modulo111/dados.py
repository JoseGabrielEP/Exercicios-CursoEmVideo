
def leiaDinheiro(): 
    while True:
        dinheiro = str(input('Insira a quantidade em dinheiro: R$')).strip().replace(',','.')
        if dinheiro.isalpha() == True or dinheiro == '':
          print(f'ERRO, "{dinheiro}" não é um valor numérico.')
        else:
            dinheiro = float(dinheiro)
            break
    return dinheiro