"""python emulator"""
import sys
from PySide2.QtWidgets import QApplication
from ui.main_window import MainWindow


if __name__ == "__main__":
    APP = QApplication(sys.argv)

    WIDGET = MainWindow()
    WIDGET.resize(1280, 720)
    WIDGET.show()

    sys.exit(APP.exec_())
