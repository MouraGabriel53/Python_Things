ano = int(input('Digite o ano em que voce nasceu: '))
idade = 2024 - ano


if idade >= 18:
    print('Voce e maior de idade!', idade)
else:
    print('Voce e menor de idade!', idade)