""" Handling file resources """

import logging
import sys


class ResourceManager(object):
    """Context manager class to handle system ressources"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.open_file = None

    def __enter__(self):
        try:
            self.open_file = open(self.filename, self.mode)
        except FileNotFoundError as e:
            logging.error("{strerror}: {filename}".format(
                strerror=e.strerror, filename=e.filename))
            sys.exit(-1)
        else:
            return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
