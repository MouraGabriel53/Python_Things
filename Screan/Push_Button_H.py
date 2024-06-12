#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Botão 1')) #Responsive module
layout.addWidget(QPushButton('Botão 2'))
window.setLayout(layout)
window.show()
app.exec()