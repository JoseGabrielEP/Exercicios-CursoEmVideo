def notas(*n, sit = True):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit == True:
        if r['Média'] >= 8:
            r['Situação'] = 'Aprovado.'
        elif r['Média'] < 7:
            r['Situação'] = 'Reprovado.'
        else:
            r['Situação'] = 'Na média.'
    return r

resp = notas(10,8.5,7,4.75,9)
print(resp)