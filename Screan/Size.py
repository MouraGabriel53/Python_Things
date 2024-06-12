#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle('Primeira Tela')
window.resize(400,300) #Width, Heidth
window.show()
app.exec()