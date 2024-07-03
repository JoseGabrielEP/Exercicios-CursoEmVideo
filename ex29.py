#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Insira a velocidade máxima atingida durante a viagem: \n'))
if velocidade > 80:
    km_percorrido = int(input('Insira quantos KMs foram percorridos ultrapassando o limite de velocidade: \n'))
    print(f'Você pagará uma multa de aproximadamente R${7.0 * km_percorrido}')
else:
    print('Você respeitou o limite de velocidade adequado!')