#Install -> pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit

app = QApplication([])
window = QWidget()
line_edit = QLineEdit(window) #Insert a writer line
window.show()
app.exec()