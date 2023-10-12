import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

VERSION_INFO = "v0.5-3-alpha"

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #add title
        self.setWindowTitle(f"WPnP Damage Calculator ({VERSION_INFO})")
        self.setFixedSize(400, 470)
        self.setWindowIcon(qtg.QIcon("_internal/resources/logo.ico"))

        # Farbpalette Background + Font
        # palette = qtg.QPalette()
        # palette.setColor(qtg.QPalette.Window, qtg.QColor(32, 33, 36))
        # self.setPalette(palette)
        # self.setStyleSheet("color: white;")

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

        attackerFormLayout.setAlignment(qtc.Qt.AlignCenter)

        # Create Picture Banner
        picture_label = qtw.QLabel()
        pixmap = qtg.QPixmap("_internal/resources/Witcher_Logo.png")
        picture_label.setPixmap(pixmap)
        picture_label.setAlignment(qtc.Qt.AlignCenter)
        attackerLayout.addWidget(picture_label)

        # Placeholder Dummy
        placeholder = qtw.QLabel()  # Leeres QLabel als Platzhalter
        attackerLayout.addWidget(placeholder)



        # Create Angreifer Label
        attacker_label = qtw.QLabel("Angreifer")
        attacker_label.setFont(qtg.QFont('Impact', 14))
        attacker_label.setAlignment(qtc.Qt.AlignCenter)
        attackerLayout.addWidget(attacker_label)

        # Create Form
        dmg_value = qtw.QLineEdit(self)
        # dmg_value.setFixedSize(70, 20)
        # dmg_value.setAlignment(qtc.Qt.AlignCenter)

        bodypart_value = qtw.QLineEdit(self)
        # bodypart_value.setFixedSize(70, 20)
        # bodypart_value.setAlignment(qtc.Qt.AlignCenter)

        armor_value = qtw.QLineEdit(self)
        # armor_value.setFixedSize(70, 20)
        # armor_value.setAlignment(qtc.Qt.AlignCenter)

        xvar_value = qtw.QLineEdit(self)
        # xvar_value.setFixedSize(70, 20)
        # xvar_value.setAlignment(qtc.Qt.AlignCenter)


        attackerFormLayout.addRow("DMG: ", dmg_value)
        attackerFormLayout.addRow("Körperteil: ", bodypart_value)

        # Placeholder Dummy
        placeholder = qtw.QLabel()  # Leeres QLabel als Platzhalter
        defenseLayout.addWidget(placeholder)

        # Defense Label
        defense_label = qtw.QLabel("Verteidiger")
        defense_label.setFont(qtg.QFont('Impact', 14))
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

        # Placeholder Dummy
        placeholder = qtw.QLabel()  # Leeres QLabel als Platzhalter
        calculateLayout.addWidget(placeholder)

        # Create Button + Final Value
        attack_button = qtw.QPushButton("Rechne", clicked = lambda: calc())
        calculateLayout.addWidget(attack_button)

        # Create Button + Final Value
        about_button = qtw.QPushButton("Info", clicked=lambda: about())
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
            elif krit_box.isChecked():
                crit = 3
            elif hkrit_box.isChecked():
                crit = 5

            dmg = float(dmg_value.text())
            body = float(bodypart_value.text())
            armor = float(armor_value.text())
            xvar = float(xvar_value.text())

            res = (dmg-armor-xvar)*body*crit
            print(res)

            if res % 1 == 0:
                show_result(int(res))
            else:
                res = round(res, 1)
                show_result(res)

        def show_result(res):
            final_label.setText(str(res))


            # (DMG - Rüstung - Wert X) * Körperteil * Krit = Final_Label

        self.show()

class AboutMe(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Made with ♡")
        self.setFixedSize(510,180)
        self.setWindowIcon(qtg.QIcon("_internal/resources/logo.ico"))

        # Farbpalette Background + Font
        # palette = qtg.QPalette()
        # palette.setColor(qtg.QPalette.Window, qtg.QColor(255, 255, 255))
        # self.setPalette(palette)
        # self.setStyleSheet("color: white;")


        # Infos
        outer_layout = qtw.QHBoxLayout()
        layout_info = qtw.QVBoxLayout()
        layout_pic = qtw.QVBoxLayout()

        layout_pic.setAlignment(qtc.Qt.AlignCenter)

        name_label = qtw.QLabel("Author: Felix Kaiser aka CosinusTangens")
        name_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(name_label)

        mail_label = qtw.QLabel("Mail: felix.ka.94@gmail.com")
        mail_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(mail_label)

        github_label = qtw.QLabel("GitHub: github.com/cosinustangens")
        github_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(github_label)

        campus_label = qtw.QLabel("Campus: Frankfurt University of Applied Sciences - FB2")
        campus_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(campus_label)

        license_label = qtw.QLabel("License: MIT License - Copyright © 2023 Felix Kaiser")
        license_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(license_label)

        # Placeholder Dummy
        placeholder = qtw.QLabel()  # Leeres QLabel als Platzhalter
        layout_info.addWidget(placeholder)

        special_label = qtw.QLabel("Special Thanks: Giuliano Micciche")
        special_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(special_label)

        version_label = qtw.QLabel(f"Version Control: {VERSION_INFO}")
        version_label.setFont(qtg.QFont('Arial', 9))
        layout_info.addWidget(version_label)

        # Picture
        picture_label = qtw.QLabel()
        pixmap = qtg.QPixmap("_internal/resources/Gemeinde.jpg")
        picture_label.setPixmap(pixmap)
        picture_label.setAlignment(qtc.Qt.AlignRight)
        layout_pic.addWidget(picture_label)



        outer_layout.addLayout(layout_info)
        outer_layout.addLayout(layout_pic)

        self.setLayout(outer_layout)


app = qtw.QApplication([])
mw = MainWindow()

#run app
app.exec_()