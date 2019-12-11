""" Input / Output Module """

import logging
import json
from pyassembler.manager.resource_manager import ResourceManager


class FileIO:
    """ File Input/Ouput class """

    @staticmethod
    def read_json(path):
        """ read json data. return python dictionary """

        with ResourceManager(path, "r") as file:
            cfg = json.load(file)
            logging.debug("config file loaded")
            return cfg

    @staticmethod
    def read_code(path):
        """ read assembler code. return python list. each element equals one line of code """

        with ResourceManager(path, "r") as file:
            code = file.read().splitlines()
            code = [str.upper(line) for line in code]
            logging.debug("code file loaded")
            return code

    @staticmethod
    def write(path, content):
        """ write machine-code to file """

        with ResourceManager(path, "w") as file:
            file.write(content)
            logging.debug("wrote file")
