import sys
from PySide2.QtWidgets import QApplication
from editor import Editor

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Editor()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
