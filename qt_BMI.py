import sys
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
    sys.exit(app.exec())