import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #add title
        self.setWindowTitle("Witcher PnP Calculator (v0.1-alpha)")
        self.setFixedSize(500, 320)

        # Create Various Layouts
        outerLayout = qtw.QVBoxLayout() # Main Layout
        attackerLayout = qtw.QVBoxLayout() # Attacker Layout
        attackerFormLayout = qtw.QFormLayout() #Attacker Form Layout
        defenseLayout = qtw.QVBoxLayout() # Defense Label
        defenseFormLayout = qtw.QFormLayout() # Defense Form Layout
        critLayout = qtw.QHBoxLayout() # Check Box Options on Crit Values
        calculateLayout = qtw.QVBoxLayout() # Final Output with Buddon (de Julie)

        attackerLayout.setAlignment(qtc.Qt.AlignBottom)
        defenseLayout.setAlignment(qtc.Qt.AlignBottom)




        #Create Angreifer Label
        attacker_label = qtw.QLabel("Angreifer")
        attacker_label.setFont(qtg.QFont('Impact', 15))
        attacker_label.setAlignment(qtc.Qt.AlignCenter)
        attackerLayout.addWidget(attacker_label)

        #Create Form
        attackerFormLayout.addRow("DMG: ", qtw.QLineEdit())
        attackerFormLayout.addRow("Körperteil: ", qtw.QLineEdit())

        #Defense Label
        defense_label = qtw.QLabel("Verteidiger")
        defense_label.setFont(qtg.QFont('Impact', 13))
        defense_label.setAlignment(qtc.Qt.AlignCenter)
        defenseLayout.addWidget(defense_label)

        # Create Defense Form
        defenseFormLayout.addRow("Rüstung: ", qtw.QLineEdit())
        defenseFormLayout.addRow("Wert X: ", qtw.QLineEdit())

        # Create Crit Boxes
        critLayout.addWidget(qtw.QCheckBox("Monster"))
        critLayout.addWidget(qtw.QCheckBox("Krit"))
        critLayout.addWidget(qtw.QCheckBox("Schwerer Krit"))

        # Create Bitton + Final Value
        attack_button = qtw.QPushButton("Rechne...")
        calculateLayout.addWidget(attack_button)

        # Create Damage Output
        final_label = qtw.QLabel("25")
        final_label.setFont(qtg.QFont('Impact', 20))
        final_label.setAlignment(qtc.Qt.AlignHCenter)
        calculateLayout.addWidget(final_label)


        #Nest Layouts
        outerLayout.addLayout(attackerLayout)
        outerLayout.addLayout(attackerFormLayout)
        outerLayout.addLayout(defenseLayout)
        outerLayout.addLayout(defenseFormLayout)
        outerLayout.addLayout(critLayout)
        outerLayout.addLayout(calculateLayout)

        self.setLayout(outerLayout)

        self.show()





app = qtw.QApplication([])
mw = MainWindow()

#run app
app.exec_()