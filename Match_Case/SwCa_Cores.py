def opcoes():
    print(' 1 - Azul\n', '2 - Branco\n', '3 - Caramelo\n', '4 - Dourado\n', '5 - Escarlate\n', '6 - Ferrugem\n', '7 - Gelo\n', '8 - Índigo\n', '9 - Jambo')

def opcao_cores(cores):
    match cores:
        case 1:
            return 'Azul'
        case 2: 
            return 'Branco'
        case 3:
            return 'Caramelo'
        case 4:
            return 'Dourado'
        case 5:
            return 'Escarlate'
        case 6:
            return 'Ferrugem'
        case 7:
            return 'Gelo'
        case 8:
            return 'Índigo'
        case 9:
            return 'Jambo'
        case _:
            return 'Opção Inválida'
        
print('\n=====Menu=====')
print(opcoes())
opcao_usuario = int(input('Digite um número de 1 a 9 para escolher uma cor: '))
print(opcao_cores(opcao_usuario))          
