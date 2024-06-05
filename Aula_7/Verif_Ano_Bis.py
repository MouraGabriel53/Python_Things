ano = int(input('Digite o ano: '))
div = ano % 4

if div == 0:
    print('O ano e bissexto')
else:
    print('o ano nao e bissexto')