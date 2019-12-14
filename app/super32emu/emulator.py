"""python emulator"""
from PySide2.QtWidgets import QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PySide2.QtCore import Qt


class Emulator(QWidget):
    """Emulator widget"""

    def __init__(self):
        QWidget.__init__(self)

        self.register_group = QGroupBox("Register")
        self.storage_group = QGroupBox("Storage")
        self.symbol_group = QGroupBox("Symbol table")

        layout = QGridLayout()
        layout.addWidget(self.register_group, 0, 0, 1, 2)
        layout.addWidget(self.storage_group, 1, 0, 1, 1)
        layout.addWidget(self.symbol_group, 1, 1, 1, 1)

        self.setLayout(layout)

        self.__create_register()

    def __create_register(self):
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

        self.register_group.setLayout(layout)
