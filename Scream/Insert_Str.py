#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
label = QLabel('Hello World', window) #Insert string
window.show()
app.exec()