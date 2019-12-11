from PySide2.QtWidgets import QHBoxLayout, QPushButton, QWidget

class Footer(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        footerBtn = QPushButton("footer")

        footerLayout = QHBoxLayout()
        footerLayout.addWidget(footerBtn)
        # footerLayout.addStretch()

        self.setLayout(footerLayout)

        self.setStyleSheet("background-color: blue;")
