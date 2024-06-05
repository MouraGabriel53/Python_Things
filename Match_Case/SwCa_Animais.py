def opcoes():
    print(' 1 - Camaleão\n', '2 - Leão\n', '3 - Gato\n', '4 - Cachorro\n', '5 - Minhoca\n', '6 - Vaca\n', '7 - Macaco\n', '8 - Pernilongo\n', '9 - Abelha4')

def opcao_animais(animais):
    match animais:
        case 1:
            return 'Camaleão'
        case 2: 
            return 'Leão'
        case 3:
            return 'Gato'
        case 4:
            return 'Cachorro'
        case 5:
            return 'Minhoca'
        case 6:
            return 'Vaca'
        case 7:
            return 'Macaco'
        case 8:
            return 'Pernilongo'
        case 9:
            return 'Abelha'
        case _:
            return 'Opção Inválida'
        
print('\n=====Menu=====')
print(opcoes())
opcao_usuario = int(input('Digite um número de 1 a 9 para escolher seu animal favorito: '))
print(opcao_animais(opcao_usuario))