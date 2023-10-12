import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

VERSION_INFO = "v0.3-1-alpha"

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #add title
        self.setWindowTitle(f"Witcher PnP Calculator ({VERSION_INFO})")
        self.setFixedSize(500, 350)


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
        dmg_value = qtw.QLineEdit(self)
        bodypart_value = qtw.QLineEdit(self)
        armor_value = qtw.QLineEdit(self)
        xvar_value = qtw.QLineEdit(self)


        attackerFormLayout.addRow("DMG: ", dmg_value)
        attackerFormLayout.addRow("Körperteil: ", bodypart_value)

        #Defense Label
        defense_label = qtw.QLabel("Verteidiger")
        defense_label.setFont(qtg.QFont('Impact', 15))
        defense_label.setAlignment(qtc.Qt.AlignCenter)
        defenseLayout.addWidget(defense_label)

        # Create Defense Form
        defenseFormLayout.addRow("Rüstung: ", armor_value)
        defenseFormLayout.addRow("Wert X: ", xvar_value)


        # Create Crit Boxes
        monster_box = qtw.QCheckBox("Monster")
        critLayout.addWidget(monster_box)

        krit_box = qtw.QCheckBox("Krit")
        critLayout.addWidget(krit_box)

        hkrit_box = qtw.QCheckBox("Schwerer Krit")
        critLayout.addWidget(hkrit_box)

        # Create Damage Output
        final_label = qtw.QLabel("-")
        final_label.setFont(qtg.QFont('Impact', 20))
        final_label.setAlignment(qtc.Qt.AlignHCenter)
        calculateLayout.addWidget(final_label)

        # Create Button + Final Value
        attack_button = qtw.QPushButton("Rechne", clicked = lambda: calc())
        calculateLayout.addWidget(attack_button)

        # Create Button + Final Value
        about_button = qtw.QPushButton("Über mich", clicked=lambda: about())
        calculateLayout.addWidget(about_button)

        # Exit Window
        exit_button = qtw.QPushButton("Beenden")
        exit_button.clicked.connect(qtw.QApplication.quit)
        calculateLayout.addWidget(exit_button)

        #Nest Layouts
        outerLayout.addLayout(attackerLayout)
        outerLayout.addLayout(attackerFormLayout)
        outerLayout.addLayout(defenseLayout)
        outerLayout.addLayout(defenseFormLayout)
        outerLayout.addLayout(critLayout)
        outerLayout.addLayout(calculateLayout)

        self.setLayout(outerLayout)

        def about():
            self.aw = AboutMe()
            self.aw.show()

        def calc():
            crit = 1
            if monster_box.isChecked():
                crit = 0.5
                print("first box")
            elif krit_box.isChecked():
                crit = 3
                print("second box")
            elif hkrit_box.isChecked():
                crit = 5
                print("third box")

            dmg = int(dmg_value.text())
            body = int(bodypart_value.text())
            armor = int(armor_value.text())
            xvar = int(xvar_value.text())

            res = (dmg-armor-xvar)*body*crit
            print(res)

            final_label.setText(str(res))
            # (DMG - Rüstung - Wert X) * Körperteil * Krit = Final_Label


        self.show()

class AboutMe(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Made with ♡")
        self.setFixedSize(450,150)


        outer_layout = qtw.QHBoxLayout()
        layout_info = qtw.QVBoxLayout()
        layout_pic = qtw.QVBoxLayout()

        name_label = qtw.QLabel("Author: Felix Kaiser aka CosinusTangens")
        layout_info.addWidget(name_label)

        mail_label = qtw.QLabel("Mail: felix.ka.94@gmail.com")
        layout_info.addWidget(mail_label)

        github_label = qtw.QLabel("GitHub: github.com/cosinustangens")
        layout_info.addWidget(github_label)

        campus_label = qtw.QLabel("Campus: Frankfurt University of Applied Sciences - FB2")
        layout_info.addWidget(campus_label)

        license_label = qtw.QLabel("License: MIT License - Copyright © 2023 Felix Kaiser")
        layout_info.addWidget(license_label)

        version_label = qtw.QLabel(f"Version Control: {VERSION_INFO}")
        layout_info.addWidget(version_label)


        outer_layout.addLayout(layout_info)

        self.setLayout(outer_layout)


app = qtw.QApplication([])
mw = MainWindow()

#run app
app.exec_()