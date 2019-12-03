import logging
import sys

logger = logging.getLogger("[assembler]")


class ResourceManager(object):
    """Context manager class to handle system ressources"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.open_file = open(self.filename, self.mode)
        except FileNotFoundError as e:
            logger.error(e.strerror + ': ' + e.filename)
            sys.exit(-1)
        else:
            return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
