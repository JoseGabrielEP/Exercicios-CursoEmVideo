#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = input('Insira o seu nome completo :\n')

maiusculo = nome.upper()
min = nome.lower()

separacao = nome.split()
juncao = ''.join(separacao)
contagem = len(juncao)

primeiro_nome = (separacao[0])
contagem_1nome = len(primeiro_nome)

resultado = f"""O nome com todas as letras maiúsculas e minúsculas fica: \n{maiusculo}\n{min}\nO nome tem {contagem} letras e o primeiro nome tem {contagem_1nome} letras."""

print(resultado)