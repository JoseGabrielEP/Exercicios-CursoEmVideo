
def aumento(n, a, format = False):
    dezPorc = (n/100)*a
    aum = n + dezPorc
    if format is False:
        return aum
    else:
        return f'R${aum}'

def desconto(n, d, format = False):
    dezPorc = (n/100)*d
    des = n - dezPorc
    if format is False:
        return des
    else:
        return f'R${des}'

def dobro(n, format = False):
    n += n
    if format is False:
        return n
    else:
        return f'R${n}'

def metade(n, format = False):
    n /= 2
    if format is False:
        return n
    else:
        return f'R${n}'
    
def resumo(n, ad , format= True):
    print(f'''
RESUMO:
METADE = {metade(n, format=True)}
DOBRO = {dobro(n, format=True)}
DESCONTO = {desconto(n, ad, format=True)}
AUMENTO =  {aumento(n, ad, format=True)}''')