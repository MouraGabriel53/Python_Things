#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

def botao_clique():
    print('Cliked button')
    
app = QApplication([])
window = QWidget()
button = QPushButton('Click Here', window) #Insert click str
button.clicked.connect(botao_clique)
window.show()
app.exec()
        