"""python emulator"""
from PySide2.QtWidgets import QHBoxLayout, QPushButton, QWidget, QDockWidget


class DockFooter(QDockWidget):
    """Dockable footer widget"""

    def __init__(self):
        QDockWidget.__init__(self)

        footer = Footer()
        self.setWidget(footer)

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


class Footer(QWidget):
    """Footer widget"""

    def __init__(self):
        QWidget.__init__(self)

        footer_button = QPushButton("footer")

        footer_layout = QHBoxLayout()
        footer_layout.addWidget(footer_button)
        # footerLayout.addStretch()

        self.setLayout(footer_layout)

        self.setStyleSheet("background-color: blue;")
