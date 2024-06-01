def opcao_regiao(regiao):
    match regiao:
        case 1:
            return 'Norte'
        case 2: 
            return 'Sul'
        case 3:
            return 'Leste'
        case 4:
            return 'Oeste'
        case _:
            return 'Opção Inválida'

pais = str(input('Digite o nome de um país: '))
print('\n=====Menu=====')
print('1 - Norte','\n2 - Sul', '\n3 - Leste', '\n4 - Oeste')
opcao_usuario = int(input('Digite um número de 1 a 4 para escolher a região: '))
print(pais+' do',opcao_regiao(opcao_usuario))