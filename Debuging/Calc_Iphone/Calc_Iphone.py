# pip install pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculadora')
        self.setFixedSize(320, 440)
        
        self.generalLayout = QVBoxLayout()
        self.setLayout(self.generalLayout)
        
        self.createDisplay()
        self.createButtons()
    
    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont('Arial', 24))
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        
        buttons = {
            'AC': (0, 0), '+/-': (0, 1), '%': (0, 2), '/': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), 'X': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3),
            '0': (4, 0), ',': (4, 2), '=': (4, 3),
        }
        
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(70, 70)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1], 1 if len(pos) == 2 else pos[2], 1 if len(pos) == 2 else pos[3])
        
        self.generalLayout.addLayout(buttonsLayout)
        
        # Estilo dos botões com bordas arredondadas
        for btn in self.buttons.values():
            if btn.text() in {'/', 'X', '-', '+', '='}:
                btn.setStyleSheet('background-color: orange; color: white; font-size: 30px; border-radius: 35px;')
            elif btn.text() in {'AC', '+/-', '%'}:
                btn.setStyleSheet('background-color: gray; color: black; font-size: 30px; border-radius: 35px;')
            else:
                btn.setStyleSheet('background-color: black; color: white; font-size: 30px; border-radius: 35px;')

class PyCalcCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == 'ERROR':
            self._view.clearDisplay()
        
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'AC'}:
                btn.clicked.connect(lambda _, bt=btnText: self._buildExpression(bt))
        
        self._view.buttons['AC'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)

def evaluateExpression(expression):
    try:
        expression = expression.replace('X', '*').replace(',', '.')
        result = str(eval(expression))
        return result
    except Exception:
        return 'ERROR'

class PyCalcUi(Calculator):
    def displayText(self):
        return self.display.text()

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def clearDisplay(self):
        self.setDisplayText('')

def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(pycalc.exec())

if __name__ == '__main__':
    main()