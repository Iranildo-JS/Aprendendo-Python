# 04- Crie um programa que leia um número e mostre sua tabuada.

num = int(input('Digite um número: '))
for i in range(11):
    print(num,' x ', i, '=', num * i)
    i = i + 1
