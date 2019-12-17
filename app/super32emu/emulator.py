"""python emulator"""
from PySide2.QtWidgets import QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QWidget, QDockWidget
from PySide2.QtCore import Qt


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
