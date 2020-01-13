"""python emulator"""
from PySide2.QtWidgets import QFrame, QPlainTextEdit, QTabWidget, QVBoxLayout, QWidget
from PySide2.QtGui import QFont


class EditorWidget(QWidget):
    """Editor widget"""

    def __init__(self):
        QWidget.__init__(self)

        self.textarea = QPlainTextEdit()
        self.textarea.setFrameShape(QFrame.NoFrame)
        self.textarea.setFont(QFont('Sans serif', 14, QFont.Medium))

        tab = QTabWidget()
        tab.addTab(self.textarea, "New File")

        editor_layout = QVBoxLayout()
        editor_layout.addWidget(tab)

        self.setLayout(editor_layout)

    def get_text(self):
        return self.textarea.toPlainText()
