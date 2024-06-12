#############################################################################Developing###############################################################################################

import sys
##from Snake_PYGAME import Snake
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QDateEdit

class FormularioInscricao(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inscrição no GameHub")

        # Criando os widgets
        self.label_titulo = QLabel("Inscreva-se no GameHub")
        self.label_nome = QLabel("Nome:")
        self.label_data_nascimento = QLabel("Data de Nascimento:")
        self.label_email = QLabel("E-mail:")
        self.label_senha = QLabel("Senha:")
        self.label_confirme_senha = QLabel("Confirme a senha:")
        
        self.lineEdit_nome = QLineEdit()
        self.lineEdit_email = QLineEdit()
        self.lineEdit_confirme_senha = QLineEdit()
        self.dateEdit_data_nascimento = QDateEdit()

        self.button_login = QPushButton("Login")

        # Criando o layout
        layout = QGridLayout()
        layout.addWidget(self.label_titulo, 0, 0, 1, 3)

        layout.addWidget(self.label_nome, 1, 0)
        layout.addWidget(self.lineEdit_nome, 1, 1, 1, 2)
        
        layout.addWidget(self.label_data_nascimento, 2, 0)
        layout.addWidget(self.dateEdit_data_nascimento, 2, 1, 1, 2)

        layout.addWidget(self.label_email, 3, 0)
        layout.addWidget(self.lineEdit_email, 3, 1, 1, 2)
        
        layout.addWidget(self.label_senha, 4, 0)
        layout.addWidget(self.lineEdit_confirme_senha, 4, 1, 1, 2)
        
        layout.addWidget(self.button_login, 5, 1, 3, 1)

        self.setLayout(layout)
        
# Criando a aplicação
app = QApplication(sys.argv)

# Criando e exibindo a janela
formulario = FormularioInscricao()
formulario.show()

# Executando a aplicação
sys.exit(app.exec())