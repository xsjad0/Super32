from PySide2.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, Qt
from PySide2.QtCore import QRegExp


class SyntaxHighlighter(QSyntaxHighlighter):
    """Super32 Syntax-Highlighter"""

    def __init__(self, parent):
        super().__init__(parent)
        self.matches = []
        self.highlighting_rules = []

        # singlelinecomment definitions
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.darkGreen)
        comment_format.setFontWeight(QFont.Medium)
        comment_pattern = QRegExp("'[^\n]*")
        self.highlighting_rules.append((comment_pattern, comment_format))

        # instruction definitions
        instruction_format = QTextCharFormat()
        instruction_format.setForeground(Qt.darkBlue)
        instruction_format.setFontWeight(QFont.Medium)
        instruction_pattern = QRegExp("\\b(SUB|ADD|AND|OR|NOR|BEQ|LW|SW)\\b")
        self.highlighting_rules.append(
            (instruction_pattern, instruction_format))

        # assembler directive definitions
        directive_format = QTextCharFormat()
        directive_format.setForeground(Qt.darkBlue)
        directive_format.setFontWeight(QFont.Medium)
        directive_pattern = QRegExp("\\b(ORG|START|END|DEFINE)\\b")
        self.highlighting_rules.append(
            (directive_pattern, directive_format))

        # label definitions
        label_format = QTextCharFormat()
        label_format.setForeground(Qt.darkCyan)
        label_format.setFontWeight(QFont.Medium)
        label_pattern = QRegExp("\\b[A-Za-z0-9_-]+:")
        self.highlighting_rules.append((label_pattern, label_format))

        # registers definitions
        register_format = QTextCharFormat()
        register_format.setForeground(Qt.darkMagenta)
        register_format.setFontWeight(QFont.Medium)
        register_pattern = QRegExp("\\bR[0-9]+")
        self.highlighting_rules.append((register_pattern, register_format))

    def highlightBlock(self, text):
        """Check textblock wether to highlight or not"""

        for (pattern, style) in self.highlighting_rules:
            index = pattern.indexIn(text)
            while index >= 0:
                self.matches.append(pattern.cap(1))
                length = pattern.matchedLength()
                self.setFormat(index, length, style)
                index = pattern.indexIn(text, index + length)
