from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
import pyqtgraph as pg

class DataEntryWidget(QWidget):
    def __init__(self):
        super().__init__()

        

def main():
    app = QApplication([])
    window = DataEntryWidget()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()



