import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #add title
        self.setWindowTitle("Die Wilde Hilde (v.0.01")

        # Set Vertical ('V') Layout
        self.setLayout(qtw.QVBoxLayout())
        my_label = qtw.QLabel("Generate License Key")

        # Change the font size of label
        #my_label.setFont(qtg.QFont('AniMe Matrix - MB_EN', 18))
        self.layout().addWidget(my_label)

        # Create Input Box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("input_field")
        my_entry.setText("Adobe CC Master COllection 2009")
        self.layout().addWidget(my_entry)

        # Create Button

        my_button = qtw.QPushButton("GENERATE DLL")
        self.layout().addWidget(my_button)


        self.show()

app = qtw.QApplication([])
mw = MainWindow()

#run app
app.exec_()