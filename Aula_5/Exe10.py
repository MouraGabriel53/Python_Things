while (1):

    import random
    numGerado = random.randint(0, 10)
    num = int(input('Adivinhe o numero: '))

    if num == numGerado:
        print('Voce acertou! O numero escolhido pelo computador e:', numGerado)
    else:
        print('Voce errou! O numero escolhido pelo computador e:', numGerado)