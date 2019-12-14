"""python emulator"""
from PySide2.QtWidgets import QAction, QFileDialog, QGridLayout, QMainWindow, QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import Slot
from editor import Editor
from emulator import Emulator
from footer import Footer
from resource_manager import ResourceManager


class MainWindow(QMainWindow):
    """This is the main window that holds the menu, the toolbar and the main widget"""

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Super 32 emulator")

        self.__create_menu()
        self.__create_toolbar()

        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

    def __create_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        new_action = QAction("New", self)
        save_action = QAction("Save", self)
        quit_action = QAction("Quit", self)

        # new.setShortcut("Ctrl+n")
        # save.setShortcut("Ctrl+S")

        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("Info")

    def __create_toolbar(self):
        tb_open = QAction(QIcon("resources/open.png"), "run", self)
        tb_save = QAction(QIcon("resources/save.png"), "save", self)
        tb_run = QAction(QIcon("resources/run.png"), "run", self)

        tb_open.triggered.connect(self.__open_file_dlg)
        tb_save.triggered.connect(self.__save_file_dlg)
        tb_run.triggered.connect(self.__run)

        tool_bar = self.addToolBar("$File")
        tool_bar.addAction(tb_open)
        tool_bar.addAction(tb_save)
        tool_bar.addAction(tb_run)

    @Slot()
    def __open_file_dlg(self):
        """Opens a file dialog to open a file"""
        path = QFileDialog.getOpenFileName(None,
                                           'Choose a file to open',
                                           '',
                                           'Text files (*.txt)')
        if path:
            with ResourceManager(path[0], "r") as file:
                result = file.read()
                self.textarea.setPlainText(result)

    @Slot()
    def __save_file_dlg(self):
        """Opens a file dialog to save a file"""
        path = QFileDialog.getSaveFileName(None,
                                           'Choose a file to save',
                                           '',
                                           'Text files (*.txt)')
        if path:
            with ResourceManager(path[0], "w") as file:
                file.write(self.textarea.toPlainText())

    @Slot()
    def __run(self):
        """Run the emulator with the written assembler"""


class MainWidget(QWidget):
    """This main widget contains all the sub-widgets"""
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
