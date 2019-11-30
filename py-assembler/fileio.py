import logging
import json
from resource_manager import ResourceManager

logger = logging.getLogger("[assembler]")


class FileIO:
    """ File Input/Ouput class """

    @staticmethod
    def read_json(path):
        """ read json data. return python dictionary """

        try:
            with ResourceManager(path, "r") as file:
                cfg = json.load(file)
                logger.info("config file loaded")
                return cfg

        except FileNotFoundError:
            logger.error("config file not found")
            sys.exit(-1)

    @staticmethod
    def read_code(path):
        """ read assembler code. return python list. each element equals one line of code """

        try:
            with ResourceManager(path, "r") as file:
                code = file.readlines()
                logger.info("code file loaded")
                return code

        except FileNotFoundError:
            logger.error("code file not found")
            sys.exit(-1)
