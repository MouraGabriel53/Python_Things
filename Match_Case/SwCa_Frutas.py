def opcoes():
    print(' 1 - Maçã\n', '2 - Banana\n', '3 - Coco\n', '4 - Tomate\n', '5 - Acerola\n', '6 - Pitanga\n', '7 - Pitaya\n', '8 - Kiwi\n', '9 - Jaca')

def opcao_frutas(frutas):
    match frutas:
        case 1:
            return 'Maçã'
        case 2: 
            return 'Banana'
        case 3:
            return 'Coco'
        case 4:
            return 'Tomate'
        case 5:
            return 'Acerola'
        case 6:
            return 'Pitanga'
        case 7:
            return 'Pitaya'
        case 8:
            return 'Kiwi'
        case 9:
            return 'Jaca'
        case _:
            return 'Opção Inválida'
        
print('\n=====Menu=====')
print(opcoes())
opcao_usuario = int(input('Digite um número de 1 a 9 para escolher uma fruta: '))
print(opcao_frutas(opcao_usuario))