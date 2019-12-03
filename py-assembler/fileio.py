import logging
import json
import sys
from resource_manager import ResourceManager

logger = logging.getLogger("[assembler]")


class FileIO:
    """ File Input/Ouput class """

    @staticmethod
    def read_json(path):
        """ read json data. return python dictionary """

        with ResourceManager(path, "r") as file:
            cfg = json.load(file)
            logger.debug("config file loaded")
            return cfg

    @staticmethod
    def read_code(path):
        """ read assembler code. return python list. each element equals one line of code """

        with ResourceManager(path, "r") as file:
            code = file.read().splitlines()
            logger.debug("code file loaded")
            return code
