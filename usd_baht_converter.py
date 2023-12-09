import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Greeting_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        
        # Label and entry for integer
        self.integer_label = QLabel(self)
        self.integer_label.setText("Enter an integer")
        vbox.addWidget(self.integer_label)
        self.integer_entry = QLineEdit(self)
        vbox.addWidget(self.integer_entry)
        
        pbt = QPushButton("USD", self)
        pbt.clicked.connect(self.greeting)
        vbox.addWidget(pbt)

        pbt1 = QPushButton("Baht", self)
        pbt1.clicked.connect(self.greeting1)
        vbox.addWidget(pbt1)
        
        self.setLayout(vbox)
        self.show()

    def greeting(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        
        # Display entered integer
        integer_label = QLabel(self)
        resultToUSD = 0.03 * float(self.integer_entry.text())
        integer_label.setText("Equivalent USD " + str(resultToUSD))
        layout.addWidget(integer_label)

        close_button = QPushButton("Close Window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        
        dialog.setLayout(layout)
        dialog.show()

    
    def greeting1(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        
        # Display entered integer
        integer_label = QLabel(self)
        resultToBaht = 30 * float(self.integer_entry.text())
        integer_label.setText("Equivalent Baht " + str(resultToBaht))
        layout.addWidget(integer_label)
        
        
        close_button = QPushButton("Close Window", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        
        dialog.setLayout(layout)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Greeting_window()
    sys.exit(app.exec())