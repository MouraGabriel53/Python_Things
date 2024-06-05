def menu():
    print('1 - Bom dia', '\n2 - Boa noite', '\n3 - Adeus', '\n4 - Olá')

def opcao_saudacao(saudacao):
    match saudacao:
        case 1:
            return 'Bom dia! '
        case 2: 
            return 'Boa noite! '
        case 3:
            return 'Adeus! '
        case 4:
            return 'Olá! '
        case _:
            return 'Opção Inválida'

nome = str(input('Digite seu nome: '))
print('\n=====Menu=====')
print(menu())
opcao_usuario = int(input('Digite um número de 1 a 4 para escolher a saudação: '))
print(opcao_saudacao(opcao_usuario) + nome)