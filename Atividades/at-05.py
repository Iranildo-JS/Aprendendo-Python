# Crie um programa que repita a mesma pergunta até que o usuário digite 0.
num = int(input(' Você tem parciência? Digite 1-SIM / 0-NÃO: '))
while num == 1:
    num = int(input(' Certeza que você tem parciência? '))
while num > 1 or num < 0:
    print('Essa resposta não é válido')
    num = int(input('Digite uma resposta válida: '))
