#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

n = int(input('Insira um número de 0 a 20: '))
extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quize','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while n not in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
    n = int(input('ERRO. Insira um número de 0 a 20: '))

print(f'O número digitado é {extenso[n]}')