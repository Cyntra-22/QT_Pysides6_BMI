import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.layout = QVBoxLayout()

        self.display_result = QLineEdit()
        self.layout.addWidget(self.display_result)

        buttons = [
             '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            'sin', 'cos', 'tan',  # Trigonometric functions
            'log', 'ln', 'sqrt',  # Logarithmic and square root
            '(', ')', 'e', 'π'
        ]

        grid_layout = QGridLayout()
        row = 0
        col = 0

        for label in buttons:
            button = QPushButton(label)
            button.clicked.connect(self.on_button_clicked)
            grid_layout.addWidget(button,row,col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)


    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try: 
                result = eval(self.display_result.text())
                self.display_result.setText(str(result))

            except Exception as e:
                self.display_result.setText("Error")

        elif text == 'C':
            self.display_result.clear()

        elif text in ('sin','cos', 'tan', 'log', 'ln', 'sqrt', '(', ')', 'e', 'π'):
            self.handle_special_function(text)

        elif text == 'e':
            self.result_display.setText(str(math.e))  # Set 'e' value
        elif text == 'π':
            self.result_display.setText(str(math.pi)) 

        else: 
            current_text = self.display_result.text()
            new_text = current_text + button.text()
            self.display_result.setText(new_text)


    def handle_special_function(self,func):
        current_text = self.display_result.text()
        if func == 'sin':
            try:
                result = math.sin(math.radians(float(current_text)))
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")

        elif func == 'cos':
            try:
                result = math.cos(math.radians(float(current_text)))
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")

        elif func == 'tan':
            try:
                result = math.tan(math.radians(float(current_text)))
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")

        elif func == 'log':
            try:
                result = math.log(float(current_text))
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        elif func == 'ln':
            try:
                result = math.log(float(current_text), math.e)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        elif func == 'sqrt':
            try:
                result = math.sqrt(float(current_text))
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")

        elif func == '(':
            self.result_display.setText(current_text + '(')  # Add opening parenthesis
        elif func == ')':
            self.result_display.setText(current_text + ')')

        else:
            self.display_result.setText(current_text)

    
def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
