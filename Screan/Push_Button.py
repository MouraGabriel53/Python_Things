#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])
window = QWidget()
button = QPushButton('Clique aqui', window) #Insert click str
window.show()
app.exec()