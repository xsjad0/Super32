"""python emulator"""
from PySide2.QtWidgets import QDockWidget, QHBoxLayout, QLabel, QWidget


class FooterDockWidget(QDockWidget):
    """Dockable footer widget"""

    def __init__(self):
        QDockWidget.__init__(self)

        self.footer = FooterWidget()
        self.setWidget(self.footer)

        self.setStyleSheet("""
        QDockWidget {
            border: 1px solid lightgray;
            titlebar-close-icon: url(close.png);
            titlebar-normal-icon: url(undock.png);
        }

        QDockWidget::title {
            background: white;
        }

        QDockWidget::close-button, QDockWidget::float-button {
            border: 1px solid transparent;
            background: white;
            padding: 0px;
        }

        QDockWidget::close-button:hover, QDockWidget::float-button:hover {
            background: gray;
        }

        QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
            padding: 1px -1px -1px 1px;
        }
        """)


class FooterWidget(QWidget):
    """Footer widget"""

    def __init__(self):
        QWidget.__init__(self)

        self.status = QLabel(
            '<img src="resources/check.png" width="22"></img>')

        self.editor_position = QLabel('<h3>0,0</h3>')

        footer_layout = QHBoxLayout()
        footer_layout.addWidget(self.status)
        footer_layout.addStretch()
        footer_layout.addWidget(self.editor_position)

        self.setLayout(footer_layout)

    def set_editor_position(self, pos_x, pos_y):
        """Sets the text for the editor position label"""
        self.editor_position.setText(
            '<h3>' + str(pos_x) + ',' + str(pos_y) + '</h3>')
