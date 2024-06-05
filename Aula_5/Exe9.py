sexo = str(input('Digite seu sexo: '))
sexoL = sexo.lower()
idade = int(input('Digite sua idade: '))

if sexoL == 'feminino' and idade >= 60:
    print('Voce pode se aposentar!')
elif sexoL == 'masculino' and idade >= 65:
    print('Voce pode se aposentar!')
else:
    print('Voce nao pode se aposentar!')