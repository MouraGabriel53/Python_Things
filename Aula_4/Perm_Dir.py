idade = int(input('Digite sua idade: '))
cartMoto = str(input('Voce possui carteira de motorista: '))

cartMotoL = cartMoto.lower()

if idade >= 18 and cartMotoL == 'sim':
    print('Voce pode dirigir!')
else:
    print('Voce nao pode dirigir!')