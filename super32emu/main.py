"""python emulator"""
import sys
from PySide2.QtWidgets import QApplication
from ui.main_window import MainWindow
from super32utils.settings.settings import Settings


if __name__ == "__main__":
    Settings.load()
    APP = QApplication(sys.argv)

    WIDGET = MainWindow()
    WIDGET.resize(1280, 720)
    WIDGET.show()

    sys.exit(APP.exec_())
