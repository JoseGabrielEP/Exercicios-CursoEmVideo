#Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

compras = ('Notebook', 2500, 'GTX 1650', 750, 'RTX 4070', 5400, 'Placa Mãe Asus', 1200, 'Mouse e Teclado', 350)

print('=-'*15)
print(f'''Mercadão:
{compras[0]} ---------- {compras[1]}
{compras[2]} ---------- {compras[3]}
{compras[4]} ---------- {compras[5]}
{compras[6]} ---------- {compras[7]}
{compras[8]} ---------- {compras[9]}''')