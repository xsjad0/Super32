"""python emulator"""
from PySide2.QtWidgets import QAction, QFileDialog, QGridLayout, QMainWindow, QWidget
from PySide2.QtGui import QIcon, Qt
from PySide2.QtCore import Slot
from super32utils.manager.resource_manager import ResourceManager
from .editor_widget import EditorWidget
from .emulator_widget import EmulatorDockWidget
from .footer_widget import FooterDockWidget
from logic.emulator import Emulator


class MainWindow(QMainWindow):
    """This is the main window that holds the menu, the toolbar and the main widget"""

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Super 32 emulator")

        self.__create_menu()
        self.__create_toolbar()

        editor_widget = EditorWidget()
        emulator_dock_widget = EmulatorDockWidget()
        footer_dock_widget = FooterDockWidget()

        self.setCentralWidget(editor_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, emulator_dock_widget)
        self.addDockWidget(Qt.BottomDockWidgetArea, footer_dock_widget)

        self.emulator = Emulator(
            editor_widget, emulator_dock_widget.get_widget(), footer_dock_widget.get_widget())

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
        tb_open = QAction(QIcon("resources/open.png"), "open", self)
        tb_save = QAction(QIcon("resources/save.png"), "save", self)
        tb_run = QAction(QIcon("resources/run.png"), "run", self)
        tb_step = QAction(QIcon("resources/step.png"), "step", self)
        tb_debug = QAction(QIcon("resources/debug.png"), "debug", self)
        tb_separator = QAction("", self)
        tb_separator.setSeparator(True)

        tb_open.triggered.connect(self.__open_file_dlg)
        tb_save.triggered.connect(self.__save_file_dlg)
        tb_run.triggered.connect(self.__run)

        tool_bar = self.addToolBar("$File")
        tool_bar.addAction(tb_open)
        tool_bar.addAction(tb_save)
        tool_bar.addAction(tb_separator)
        tool_bar.addAction(tb_run)
        tool_bar.addAction(tb_step)
        tool_bar.addAction(tb_debug)

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
        """Runs the emulator"""
        self.emulator.run()
