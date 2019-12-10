from emulator import Emulator
from functools import partial
from resource_manager import ResourceManager
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QFileDialog, QFrame, QHBoxLayout, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from PySide2.QtGui import QFont, QIcon


class Editor(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Super 32 emulator")

        self.textareaText = "asdf"

        self.menuOpen = QPushButton()
        self.menuOpen.setIcon(QIcon("resources/open.png"))
        self.menuOpen.clicked.connect(self.openFileDlg)

        self.menuSave = QPushButton()
        self.menuSave.setIcon(QIcon("resources/save.png"))
        self.menuSave.clicked.connect(self.saveFileDlg)

        self.menuRun = QPushButton()
        self.menuRun.setIcon(QIcon("resources/run.png"))
        self.menuRun.clicked.connect(self.runDlg)

        self.menu = QHBoxLayout()
        self.menu.addWidget(self.menuOpen)
        self.menu.addWidget(self.menuSave)
        self.menu.addWidget(self.menuRun)
        self.menu.addStretch()
        self.menu.setContentsMargins(5, 5, 0, 0)

        self.textarea = QPlainTextEdit(self)
        self.textarea.setFrameShape(QFrame.NoFrame)
        self.textarea.setFont(QFont('Sans serif', 14, QFont.Medium))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.menu)
        self.mainLayout.addWidget(self.textarea)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mainLayout)

    @Slot()
    def openFileDlg(self):
        path = QFileDialog.getOpenFileName(None,
                                           'Choose a file to open',
                                           '',
                                           'Text files (*.txt)')
        if path:
            with ResourceManager(path[0], "r") as file:
                f = file.read()
                self.textarea.setPlainText(f)

    @Slot()
    def saveFileDlg(self):
        pass
        path = QFileDialog.getSaveFileName(None,
                                           'Choose a file to save',
                                           '',
                                           'Text files (*.txt)')
        if path:
            with ResourceManager(path[0], "w") as file:
                file.write(self.textarea.toPlainText())

    @Slot()
    def runDlg(self):
        Emulator.run()
