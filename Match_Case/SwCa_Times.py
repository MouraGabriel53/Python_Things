def opcoes():
    print(' 1 - Corinthians\n', '2 - Palmeiras\n', '3 - Flamengo\n', '4 - Botafogo\n', '5 - Íbis\n', '6 - São Paulo\n', '7 - Real Madrid\n', '8 - Barcelona\n', '9 - União Mogi')

def opcao_times(times):
    match times:
        case 1:
            return 'Corinthians'
        case 2: 
            return 'Palmeiras'
        case 3:
            return 'Flamengo'
        case 4:
            return 'Botafogo'
        case 5:
            return 'Íbis'
        case 6:
            return 'São Paulo'
        case 7:
            return 'Real Madrid'
        case 8:
            return 'Barcelona'
        case 9:
            return 'União Mogi'
        case _:
            return 'Opção Inválida'
        
print('\n=====Menu=====')
print(opcoes())
opcao_usuario = int(input('Digite um número de 1 a 9 para escolher o campeão da Champions: '))
print(opcao_times(opcao_usuario))