idade = int(input('Digite sua idade: '))
sexo = str(input('Digite seu sexo: '))

sexoL = sexo.lower()

if sexoL == 'feminino' and idade >= 60:
    print('Voce pode se aposentar por idade!')
elif sexoL == 'masculino' and idade >= 65:
    print('Voce pode se aposentar!')
else:
    print('Voce ainda nao pode solicitar a aposentadoria por idade!')