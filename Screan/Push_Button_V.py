#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication([])
window = QWidget()
layout = QHBoxLayout()
layout.addWidget(QPushButton('Esquerda')) #Responsive module
layout.addWidget(QPushButton('Direita'))
window.setLayout(layout)
window.show()
app.exec()