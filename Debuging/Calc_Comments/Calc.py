# Importa o módulo sys, que fornece acesso a algumas variáveis e funções usadas ou mantidas pelo interpretador Python
import sys

#Resumo das Importações
#sys: Necessário para passar argumentos de linha de comando ao QApplication.
#QApplication: Gerencia a aplicação e o loop de eventos.
#QVBoxLayout: Organiza widgets verticalmente.
#QLineEdit: Campos de entrada para texto.
#QPushButton: Botão clicável.
#QLabel: Exibe texto ou imagens.
#QWidget: Base para todos os widgets, usado como janela principal.
#Por que Importamos Esses Itens?
#Ao importar essas classes, podemos criar e organizar a interface gráfica da aplicação, obter entradas do usuário, executar ações com essas entradas (como calcular a soma), e exibir os resultados de forma organizada.

#Essas importações permitem que você utilize a rica funcionalidade do PyQt6 para construir uma aplicação GUI funcional e interativa.

# Importa classes do módulo QtWidgets do PyQt6, que são usadas para criar a interface gráfica da aplicação
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget


# Função para calcular a soma dos números inseridos
def calculate_sum():
    # Obtém os valores dos campos de texto, converte para float e calcula a soma, depois atualiza o rótulo com o resultado
    result_label.setText(f"Resultado: {float(line_edit1.text()) + float(line_edit2.text())}")
def calculate_sub():
    result_label.setText(f"Resultado: {float(line_edit1.text()) - float(line_edit2.text())}")
def calculate_multp():
    result_label.setText(f"Resultado: {float(line_edit1.text()) * float(line_edit2.text())}")
def calculate_div():
     result_label.setText(f"Resultado: {float(line_edit1.text()) / float(line_edit2.text())}")
      
# Cria a aplicação Qt
app = QApplication(sys.argv)
# Cria a janela principal
window = QWidget()
# Cria um layout vertical e associa à janela
layout = QVBoxLayout(window)

# Cria o primeiro campo de texto para inserir um número
line_edit1 = QLineEdit()
line_edit1.setPlaceholderText("Digite um número")  # Texto de dica no campo de texto
layout.addWidget(line_edit1)  # Adiciona o campo de texto ao layout

# Cria o segundo campo de texto para inserir outro número
line_edit2 = QLineEdit()
line_edit2.setPlaceholderText("Digite outro número")  # Texto de dica no campo de texto
layout.addWidget(line_edit2)  # Adiciona o campo de texto ao layout

# Cria o botão para calcular a soma
button = QPushButton('Soma')
button.clicked.connect(calculate_sum)  # Conecta o clique do botão à função de calcular a soma
layout.addWidget(button)  # Adiciona o botão ao layout

# Cria o botão para calcular a subtração
button = QPushButton('Subtração')
button.clicked.connect(calculate_sub)  # Conecta o clique do botão à função de calcular a soma
layout.addWidget(button)  # Adiciona o botão ao layout

# Cria o botão para calcular a multiplicação
button = QPushButton('Multiplicação')
button.clicked.connect(calculate_multp)  # Conecta o clique do botão à função de calcular a soma
layout.addWidget(button)  # Adiciona o botão ao layout

# Cria o botão para calcular a divisão
button = QPushButton('Divisão')
button.clicked.connect(calculate_div)  # Conecta o clique do botão à função de calcular a soma
layout.addWidget(button)  # Adiciona o botão ao layout

# Cria o rótulo para exibir o resultado
result_label = QLabel('')
layout.addWidget(result_label)  # Adiciona o rótulo ao layout


# Exibe a janela principal
window.show()

# Inicia o loop de eventos da aplicação
sys.exit(app.exec())
