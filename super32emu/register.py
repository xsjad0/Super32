"""python emulator"""
from PySide2.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class Register(QWidget):
    """Register widget"""

    def __init__(self, text):
        QWidget.__init__(self)

        self.label = QLabel()

        if(text):
            self.label.setText(text)

        text_input = QLineEdit()
        text_input.setFixedWidth(80)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(text_input)

        self.setLayout(layout)

    def set_text(self, text):
        """Set the text of the label"""
        self.label.setText(text)
