#Creating a bank
class Contabancaria:
    def __init__ (self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor} realizado com sucesso na conta de{self.titular}.')
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso na conta{self.titular}.')
        else:
            print('Saldo insuficiente.')

    def mostrar_saldo(self):
        print(f'Saldo atual de {self.titular}: R${self.saldo}.')
    
#Creating accounts
contas = {
    'Gabriel': Contabancaria('Gabriel', 300),
    'Gustavo': Contabancaria('Gustavo', 300)
}

#Userface
def banco_interface():
        while(1):
            titular = input('Digite o nome do cliente (Gabriel ou Gustavo) ou sair para encerrar: ')
            if titular == 'sair': 
                break
            if titular in contas:
                acao = input('Digite saldo para verifcar o saldo, depositar para depositar ou sacar para sacar: ')
            if acao == "saldo":
                contas[titular].mostrar_saldo()
            elif acao in ['depositar', 'sacar']:
                valor = float(input('Digite o valor: R$'))
                if acao == 'depositar':
                    contas[titular].depositar(valor)
                else: 
                    contas[titular].sacar(valor)
            else:
                print('Ação inválida!')
        else:
            print('Cliente não encontrado!')
        
#Call the function userinterface
banco_interface() 

            
            