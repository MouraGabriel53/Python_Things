valorTotal = float(input('Digite o valor total de sua compra: '))

if valorTotal <= 100:
    print('Sem desconto')
elif valorTotal >= 100.1 and valorTotal <= 500: 
    print('5% desconto')
elif valorTotal >= 500.1 and valorTotal <= 1000: 
    print('10% desconto')
else:
    print('15% de desconto')