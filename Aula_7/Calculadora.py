num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
print('==========')
operacao = str(input('Soma\nSubtracao\nMultiplicacao\nDivisao\n===========\nEscolha a opercao que deseja fazer: '))
operacaoL = operacao.lower()

if operacaoL == 'soma':
    print('A soma e:', num1+num2)
elif operacaoL == 'subtracao':
    print('A subtracao e:', num1-num2)
elif operacaoL == 'multiplicacao':
    print('A multiplicacao e:', num1*num2)
else:
    print('A divisao e:', num1/num2)