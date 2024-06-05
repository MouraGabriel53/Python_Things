capital = float(input('Digite o capital inicial: '))
juros = float(input('Digite o juros: '))
tempo = float(input('Digite o tempo: '))
valorJuros = (juros/100) * capital
valorTotal = (valorJuros + capital) * tempo

print('O montante final e:', valorTotal)