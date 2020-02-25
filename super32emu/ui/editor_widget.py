"""python emulator"""
from PySide2.QtWidgets import QFrame, QPlainTextEdit, QTabWidget, QVBoxLayout, QWidget
from PySide2.QtGui import QFont
from PySide2.QtCore import Slot, Signal


class EditorWidget(QWidget):
    """Editor widget"""

    tab_count = 0

    def __init__(self):
        QWidget.__init__(self)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.__close_tab)
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def new_tab(self, title=None, content=""):
        EditorWidget.tab_count += 1
        textarea = QPlainTextEdit()
        textarea.setFrameShape(QFrame.NoFrame)
        textarea.setFont(QFont("Fira Code", 12, QFont.Normal))
        textarea.setPlainText(content)
        tab_index = self.tabs.addTab(
            textarea,
            "Untitled-{tab_count}".format(tab_count=EditorWidget.tab_count)
        )
        if title:
            self.tabs.setTabText(tab_index, title)
        self.tabs.setCurrentIndex(tab_index)

    @Slot()
    def __close_tab(self, index):
        self.tabs.removeTab(index)
