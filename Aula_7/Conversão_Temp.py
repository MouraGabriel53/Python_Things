print('===== Conversão de Temperatura =====')
print('Digite 1 -> °C para °F\nDigite 2 -> °F para °C')
op = int(input('Digite o numero: '))

if op == 1:
    celsius = float(input('Digite a temperatura em °C: '))
    conver_C_F = (celsius * 9/5) + 32
    print('O valor e:', '%.2f'% conver_C_F, '°F')
else:
    fahrenheit = float(input('Digite a temperatura em °F: '))
    conver_F_C = (fahrenheit - 32) * 5/9
    print('O valor e:', '%.2f'% conver_F_C, '°C')
