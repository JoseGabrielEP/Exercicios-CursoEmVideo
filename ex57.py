# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


#variáveis
sexo = input('Qual o seu sexo [M/F]: ').upper().strip()
limitador = 'mfMF'

#laço e condicional:
while sexo not in limitador:
   sexo = input('DÍGITO INVÁLIDO. Qual o seu sexo [M/F]:  ').upper().strip()

#conclusão
print('-' * 30)
print(f'Pronto, sexo {sexo} registrado.')