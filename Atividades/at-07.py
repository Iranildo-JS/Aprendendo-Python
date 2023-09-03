# crie um programa que simule o sorteio da mega-sena.

# Usando a biblioteca ramdom pra sorteia os números da mega.

from random import randint
num1 = randint(1,60)
num2 = randint(1,60)
num3 = randint(1,60)
num4 = randint(1,60)
num5 = randint(1,60)
num6 = randint(1,60)

# Função para garantir que o programa não cometa o erro de repetição de números.

while num2 == num1:
    num2 = randint(1,60)

while num3 == num1 or num3 == num2:
    num3 = randint(1,60)

while num4 == num1 or num4 == num2 or num4 == num3:
    num4 = randint(1,60)

while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    num5 = randint(1,60)

while num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
    num6 = randint(1,60)

# Tela e resultado final.

print('\t\t\t\t\t\t', '_' * 13)
print('\t\t\t\t\t\t', '| MEGA-SENA |')
print('\t\t\t\t\t', '=' * 30)
print('\t\t\t\t\t  ({}) ({}) ({}) ({}) ({}) ({})'.format(num1, num2, num3, num4, num5, num6))
print('\t\t\t\t\t','=' * 30)
