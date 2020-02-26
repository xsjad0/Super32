"""python emulator"""
from PySide2.QtWidgets import QFrame, QPlainTextEdit, QTabWidget, QVBoxLayout, QWidget
from PySide2.QtGui import QFont
from PySide2.QtCore import Slot, Signal
from super32emu.logic.highlighter import SyntaxHighlighter


class EditorWidget(QWidget):
    """Editor widget"""

    tab_count = 0

    def __init__(self):
        QWidget.__init__(self)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.__on_close_tab)
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def new_tab(self, title="", content=""):
        """Append new tab"""

        EditorWidget.tab_count += 1
        editor = QPlainTextEdit()
        highlighter = SyntaxHighlighter(editor.document())

        editor.setFrameShape(QFrame.NoFrame)
        editor.setFont(QFont("Fira Code", 10, QFont.Normal))
        editor.setPlainText(content)
        tab_index = self.tabs.addTab(
            editor,
            "Untitled-{tab_count}".format(tab_count=EditorWidget.tab_count)
        )

        if title:
            self.tabs.setTabText(tab_index, title)
        self.tabs.setCurrentIndex(tab_index)

    @Slot()
    def __on_close_tab(self, index):
        """Close tab on button-press"""
        self.tabs.removeTab(index)
