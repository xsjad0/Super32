from PySide2.QtWidgets import QAction, QFileDialog, QGridLayout, QMainWindow, QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import Slot
from editor import Editor
from emulator import Emulator
from footer import Footer
from resource_manager import ResourceManager


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Super 32 emulator")

        self.createMenu()
        self.createToolbar()

        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)

    def createMenu(self):
        bar = self.menuBar()

        fileMenu = bar.addMenu("File")
        newAction = QAction("New", self)
        saveAction = QAction("Save", self)
        quitAction = QAction("Quit", self)

        # new.setShortcut("Ctrl+n")
        # save.setShortcut("Ctrl+S")

        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(quitAction)

        editMenu = bar.addMenu("Edit")
        editMenu.addAction("Copy")
        editMenu.addAction("Paste")

        helpMenu = bar.addMenu("Help")
        helpMenu.addAction("Info")

    def createToolbar(self):
        tbOpen = QAction(QIcon("resources/open.png"), "run", self)
        tbSave = QAction(QIcon("resources/save.png"), "save", self)
        tbRun = QAction(QIcon("resources/run.png"), "run", self)

        tbOpen.triggered.connect(self.openFileDlg)
        tbSave.triggered.connect(self.saveFileDlg)
        tbRun.triggered.connect(self.runDlg)

        tb = self.addToolBar("$File")
        tb.addAction(tbOpen)
        tb.addAction(tbSave)
        tb.addAction(tbRun)

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
        pass


class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        editor = Editor()
        emulator = Emulator()
        footer = Footer()

        layout = QGridLayout()
        layout.addWidget(editor, 0, 0, 1, 1)
        layout.addWidget(emulator, 0, 1, 1, 1)
        layout.addWidget(footer, 1, 0, 1, 2)

        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
