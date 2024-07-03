# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('GRÊMIO','INTERNACIONAL','CHAPECOENSE','VASCO','CORINTHIANS','FLAMENGO','CRUZEIRO','CAXIAS','BAHIA','FLUMINENSE')

print(f'Os 5 primeiros times são {times[0:5]}')
print('=-'*15)
print(f'Os 4 últimos times são {times[5:]}')
print('=-'*15)
print(f'Os times em ordem são {sorted(times)}')
print('=-'*15)
print(f'O Chapecoense está na posição {times.index('CHAPECOENSE') + 1}')