nota1 = float(input('Digite a sua nota 1: '))
nota2 = float(input('Digite a sua nota 2: '))
med = (nota1+nota2)/2

if med >= 6:
    print('Aprovado:', med)
else:
    print('Reprovado:', med)