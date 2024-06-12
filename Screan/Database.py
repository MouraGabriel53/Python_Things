#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])
janela = QWidget()
janela.setWindowTitle('Primeira Tela')
janela.show()
app.exec()