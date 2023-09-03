# crie um programa que leia a idade do usuário e mostre se ele tem direito de votação.

idade = int(input('Digite sua idade: '))

# Estrutura de condição.
# Analisando a variável para determinar a resposta.

if idade >= 18 and idade <= 69:
    print('Seu voto é obrigatório. ')
elif idade >=16 and idade <= 17 or idade > 69:
    print('Seu voto é opcional.')
else:
    print('Você não tem idade suficiente para votar. ')
