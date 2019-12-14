"""python emulator"""
from PySide2.QtWidgets import QHBoxLayout, QPushButton, QWidget


class Footer(QWidget):
    """Footer widget"""

    def __init__(self):
        QWidget.__init__(self)

        footer_button = QPushButton("footer")

        footer_layout = QHBoxLayout()
        footer_layout.addWidget(footer_button)
        # footerLayout.addStretch()

        self.setLayout(footer_layout)

        self.setStyleSheet("background-color: blue;")
