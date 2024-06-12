from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
label = QLabel('', window)
button = QPushButton('Clique aqui!', window)

def change_label_text():
    label.setText('Você pegou vírus!')

button.clicked.connect(change_label_text)
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec()