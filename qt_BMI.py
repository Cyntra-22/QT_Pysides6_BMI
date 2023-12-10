'''import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import math

class Greeting_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        
        # Label and entry for integer
        self.integer_label = QLabel(self)
        self.integer_label.setText("Enter your height(cm) and weight(kg): ")
        vbox.addWidget(self.integer_label)
        self.integer_entry = QLineEdit(self)
        vbox.addWidget(self.integer_entry)

        self.integer_entry1 = QLineEdit(self)
        vbox.addWidget(self.integer_entry1)
        
        pbt = QPushButton("Calculate", self)
        pbt.clicked.connect(self.calculateBMI)
        vbox.addWidget(pbt)
        
        self.setLayout(vbox)
        self.show()

    def calculateBMI(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        
        # Display entered integer
        integer_label = QLabel(self)
        integer_label1 = QLabel(self)
        weight = float(self.integer_entry.text())
        height = (int(self.integer_entry1.text()) / 100 ) * (int(self.integer_entry1.text()) /100)
        result = round((weight / float(height)),2)
        if(result < 18.5):
            integer_label.setText("The result is: " + str(result))
            integer_label1.setText("You are underweight.")

        elif (result > 18.5 ) and (result < 24.9):
            integer_label.setText("The result is: " + str(result))
            integer_label1.setText("You are normal.")

        elif (result > 25 ) and (result < 29.9):
            integer_label.setText("The result is: " + str(result))
            integer_label1.setText("You are overweight.")

        else:
            integer_label.setText("The result is: " + str(result))
            integer_label1.setText("You are obese.")


        layout.addWidget(integer_label)
        layout.addWidget(integer_label1)

        close_button = QPushButton("Close Window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        
        dialog.setLayout(layout)
        dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Greeting_window()
    sys.exit(app.exec())'''



import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Currency Converter")
        self.setGeometry(100, 100, 400, 200)

        # Labels to display selected currencies
        self.from_currency_label = QLabel("From: ")
        self.to_currency_label = QLabel("To: ")
        
        # Buttons to select currencies
        self.from_currency_button = QPushButton("Select From Currency")
        self.to_currency_button = QPushButton("Select To Currency")
        
        # Connecting button clicks to functions
        self.from_currency_button.clicked.connect(self.select_from_currency)
        self.to_currency_button.clicked.connect(self.select_to_currency)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.from_currency_label)
        layout.addWidget(self.from_currency_button)
        layout.addWidget(self.to_currency_label)
        layout.addWidget(self.to_currency_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def select_from_currency(self):
        # Implement logic for selecting 'from' currency
        selected_currency = "USD"  # Replace with your logic to select currency
        self.from_currency_label.setText(f"From: {selected_currency}")

    def select_to_currency(self):
        # Implement logic for selecting 'to' currency
        selected_currency = "EUR"  # Replace with your logic to select currency
        self.to_currency_label.setText(f"To: {selected_currency}")


def main():
    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
