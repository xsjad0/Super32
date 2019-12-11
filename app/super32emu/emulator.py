from PySide2.QtWidgets import QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PySide2.QtCore import Qt


class Emulator(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.registerGroup = QGroupBox("Register")
        self.storageGroup = QGroupBox("Storage")
        self.symbolGroup = QGroupBox("Symbol table")

        layout = QGridLayout()
        layout.addWidget(self.registerGroup, 0, 0, 1, 2)
        layout.addWidget(self.storageGroup, 1, 0, 1, 1)
        layout.addWidget(self.symbolGroup, 1, 1, 1, 1)

        self.setLayout(layout)

        self.createRegister()

    def createRegister(self):
        layout = QHBoxLayout()

        r1 = QLineEdit()
        r2 = QLineEdit()
        r3 = QLineEdit()
        r4 = QLineEdit()

        layout.addWidget(r1)
        layout.addWidget(r2)
        layout.addWidget(r3)
        layout.addWidget(r4)
        layout.setAlignment(Qt.AlignTop)

        self.registerGroup.setLayout(layout)
