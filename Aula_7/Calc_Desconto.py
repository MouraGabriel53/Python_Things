preço = float(input('Digite o valor total da compra: '))
desconto = float(input('Digite o valor do desconto: '))
preçoDesconto = (desconto/100) * preço
valorFinal = preço - preçoDesconto
print('O valor com desconto e:', '%.2F'% valorFinal)