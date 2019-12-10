
from PySide2.QtWidgets import QPushButton, QDialog


class Emulator(QDialog):
    def __init__(self, parent=None):
        super(Emulator, self).__init__(parent)

        self.setWindowTitle("Emulator")

        self.button = QPushButton("Test")

    @staticmethod
    def run():
        emulator = Emulator()
        emulator.exec_()
