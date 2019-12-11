import sys
from mainWindow import MainWindow
from PySide2.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.resize(1280, 720)
    widget.show()

    sys.exit(app.exec_())
