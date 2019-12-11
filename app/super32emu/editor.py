from PySide2.QtWidgets import QFrame, QPlainTextEdit, QTabWidget, QVBoxLayout, QWidget
from PySide2.QtGui import QFont


class Editor(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        textarea = QPlainTextEdit()
        textarea.setFrameShape(QFrame.NoFrame)
        textarea.setFont(QFont('Sans serif', 14, QFont.Medium))

        tab = QTabWidget()
        tab.addTab(textarea, "New File")

        editorLayout = QVBoxLayout()
        editorLayout.addWidget(tab)

        self.setLayout(editorLayout)
