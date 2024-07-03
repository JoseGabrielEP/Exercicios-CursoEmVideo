#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.error
import urllib.request


def openSites(link):
    try:
       abertura = urllib.request.urlopen(link)
    except:
        print('O SITE NÃO ESTÁ ACESSÍVEL!')
    else:
        print('O SITE ESTÁ ACESSÍVEL!')
    finally:
        print('Volte sempre!')



openSites('https://www.pudim.com.br')