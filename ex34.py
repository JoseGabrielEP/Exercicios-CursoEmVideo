#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250.00,
#calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Insira o seu salário: \n'))
if salario <= 1250:
    aumento15 = ( salario / 100) * 15 + salario
    print(f'O seu salário com aumento de 15% ficará R${aumento15}!')
else:
    aumento10 = ( salario / 100) * 10 + salario
    print(f'O seu salário com aumento de 10% ficará R${aumento10}!')
print('-' * 30)