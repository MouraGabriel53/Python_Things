peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)

if imc < 18.5:
    print('Voce esta abaixo do peso:', imc)
elif imc >= 18.5 and imc <= 24.9:
    print('Voce esta com o peso normal:', imc)
elif imc >= 25 and imc <= 29.9:
    print('Voce esta com sobre peso:', imc)
elif imc >= 30:
    print('Voce esta com obesidade:', imc )
else:
    print('Voce esta com obesidade extrema:', imc)