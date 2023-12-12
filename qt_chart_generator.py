from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
import pyqtgraph as pg

class DataEntryWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edits_horizontal = []  
        self.line_edits_vertical = []   
        self.data_list_horizontal = []   
        self.data_list_vertical = []     

        main_layout = QHBoxLayout(self)

        # First column for horizontal data
        horizontal_layout = QVBoxLayout()
        add_horizontal_button = QPushButton("Add Horizontal Data", self)
        add_horizontal_button.clicked.connect(self.create_horizontal_line_edit)
        horizontal_layout.addWidget(add_horizontal_button)
        main_layout.addLayout(horizontal_layout)

        # Second column for vertical data
        vertical_layout = QVBoxLayout()
        add_vertical_button = QPushButton("Add Vertical Data", self)
        add_vertical_button.clicked.connect(self.create_vertical_line_edit)
        vertical_layout.addWidget(add_vertical_button)
        main_layout.addLayout(vertical_layout)

        # Plot area
        self.graph_widget = pg.PlotWidget()
        main_layout.addWidget(self.graph_widget)

        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.retrieve_data)
        main_layout.addWidget(submit_button)

        self.setLayout(main_layout)

    def create_horizontal_line_edit(self):
        new_line_edit = QLineEdit(self)
        self.line_edits_horizontal.append(new_line_edit)
        self.layout().itemAt(0).layout().insertWidget(self.layout().itemAt(0).layout().count() - 1, new_line_edit)

    def create_vertical_line_edit(self):
        new_line_edit = QLineEdit(self)
        self.line_edits_vertical.append(new_line_edit)
        self.layout().itemAt(1).layout().insertWidget(self.layout().itemAt(1).layout().count() - 1, new_line_edit)

    def retrieve_data(self):

        self.data_list_horizontal.clear()
        self.data_list_vertical.clear()

        
        for line_edit in self.line_edits_horizontal:
            self.data_list_horizontal.append(float(line_edit.text()))

        for line_edit in self.line_edits_vertical:
            self.data_list_vertical.append(float(line_edit.text()))

       
        self.graph_widget.clear()

        self.graph_widget.plot(self.data_list_horizontal, self.data_list_vertical, symbol='o')

def main():
    app = QApplication([])
    window = DataEntryWidget()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()



