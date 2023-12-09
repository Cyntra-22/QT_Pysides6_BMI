import sys
from PySide6.QtWidgets import*
from PySide6.QtCore import *
import time

class Simple_timer_window(QWidget):

    def __init__(self):
        QWidget.__init__(self,None)
        self.num = 0

        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)

        timer = QTimer(self)
        timer.timeout.connect(self.updateValue) #every 500 milliseconds will be called the updatevalue function
        timer.start(500)
        self.setLayout(vbox)
        self.show()


    def updateValue(self):
        self.num = time.strftime("%X") #to get the current time in a formatted string

        self.label.setText(str(self.num))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Simple_timer_window()

    sys.exit(app.exec())