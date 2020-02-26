"""python emulator"""
from PySide2.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget
from PySide2.QtGui import QFont


class RegisterWidget(QWidget):
    """Register widget"""

    def __init__(self, text):
        QWidget.__init__(self)

        self.label = QLabel()

        if text:
            self.label.setText(text)

        self.text_input = QLineEdit()
        self.text_input.setFixedWidth(35)
        self.text_input.setFont(QFont('Fira Code', 8, QFont.Medium))

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addStretch()

        self.setLayout(layout)

    def set_text(self, text):
        """Set the text of the label"""
        self.label.setText(text)

    def set_value(self, value):
        """Set the value of the register"""
        self.text_input.setText(value)
