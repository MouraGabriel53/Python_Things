#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPalette, QColor

app = QApplication([])
window = QWidget()
window.setWindowTitle('Primeira Tela')
palette = window.palette()
palette.setColor(QPalette.ColorRole.Window, QColor('black')) #Set window color
window.setPalette(palette)
window.show()
app.exec()