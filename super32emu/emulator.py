"""python emulator"""
from PySide2.QtWidgets import QDockWidget, QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Qt
from PySide2.QtCore import Slot
from register import Register
from PySide2.QtGui import QIcon


class DockEmulator(QDockWidget):
    """Dockable emulator widget"""

    def __init__(self):
        QDockWidget.__init__(self)

        emulator = Emulator()
        self.setWidget(emulator)

        self.setStyleSheet("""
            QDockWidget {
                border: 1px solid lightgray;
                titlebar-close-icon: url(close.png);
                titlebar-normal-icon: url(undock.png);
            }

            QDockWidget::title {
                background: white;
            }

            QDockWidget::close-button, QDockWidget::float-button {
                border: 1px solid transparent;
                background: white;
                padding: 0px;
            }

            QDockWidget::close-button:hover, QDockWidget::float-button:hover {
                background: gray;
            }

            QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
                padding: 1px -1px -1px 1px;
            }
        """)


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

        self.__create_register_group()

    def __create_register_group(self):
        self.index = 0
        self.register = []

        for i in range(32):
            self.register.append(Register('r' + str(i)))

        self.register_layout = QHBoxLayout()
        self.register_layout.addWidget(self.register[self.index])
        self.register_layout.addWidget(self.register[self.index + 1])
        self.register_layout.addWidget(self.register[self.index + 2])
        self.register_layout.addWidget(self.register[self.index + 3])

        back = QPushButton()
        back.setIcon(QIcon("resources/back.png"))
        back.setFlat(True)
        back.clicked.connect(self.__previous_register)
        forth = QPushButton()
        forth.setIcon(QIcon("resources/forth.png"))
        forth.setFlat(True)
        forth.clicked.connect(self.__next_register)

        arrows_layout = QHBoxLayout()
        arrows_layout.addWidget(back)
        arrows_layout.addWidget(forth)

        register_arrows_layout = QHBoxLayout()
        register_arrows_layout.addLayout(self.register_layout)
        register_arrows_layout.addLayout(arrows_layout)
        register_arrows_layout.setAlignment(Qt.AlignTop)

        program_counter = Register('Pc')

        register_group_layout = QVBoxLayout()
        register_group_layout.addLayout(register_arrows_layout)
        register_group_layout.addWidget(program_counter)

        self.register_group.setLayout(register_group_layout)

    @Slot()
    def __next_register(self):
        if self.index == 28:
            return

        self.index += 1

        self.__update_register()

    @Slot()
    def __previous_register(self):
        if self.index == 0:
            return

        self.index -= 1

        self.__update_register()

    def __update_register(self):
        for i in reversed(range(self.register_layout.count())):
            self.register_layout.itemAt(i).widget().setParent(None)

        self.register_layout.addWidget(self.register[self.index])
        self.register_layout.addWidget(self.register[self.index + 1])
        self.register_layout.addWidget(self.register[self.index + 2])
        self.register_layout.addWidget(self.register[self.index + 3])
