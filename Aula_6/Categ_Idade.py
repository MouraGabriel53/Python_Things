idade = int(input('Digite sua idade: '))

if idade >= 5 and idade <= 7:
    print('Categoria: Infantil A')
elif idade >= 8 and idade <= 11:
    print('Categoria: Infantil B')
elif idade >= 12 and idade <= 13:
    print('Categoria: Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Categoria: juvenil B')
else:
    print('Categoria: Adulto')
