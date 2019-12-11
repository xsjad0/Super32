"""
Enum Assembler-Directives
"""

from enum import Enum, auto


class AssemblerDirectives(Enum):
    START = auto()
    END = auto()
    ORG = auto()
    DEFINE = auto()

    @classmethod
    def to_string(cls):
        return "{START},{END},{ORG},{DEFINE}".format(
            START=cls.START.name,
            END=cls.END.name,
            ORG=cls.ORG.name,
            DEFINE=cls.DEFINE.name
        )
