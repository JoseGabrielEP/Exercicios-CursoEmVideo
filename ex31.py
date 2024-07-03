#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Insira a distância total da viagem: \n'))
if distancia > 200:
    print(f'O custo da viagem será de R${distancia * 0.45}')
else: 
    print(f'O custo da viagem será de R${distancia * 0.50}')
print('-OBRIGADO-PELA-PREFERÊNCIA-' * 5)