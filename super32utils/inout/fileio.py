""" Input / Output Module """

import logging
import json
from super32utils.manager.resource_manager import ResourceManager


class FileIO:
    """ File Input/Ouput class """

    @staticmethod
    def read_json(path):
        """ read json data. return python dictionary """

        cfg = {}
        with ResourceManager(path, "r") as file:
            cfg = json.load(file)
            logging.debug("config file loaded")
        return cfg

    @staticmethod
    def read_code(path):
        """ read assembler code. return python list. each element equals one line of code """
        code = []
        with ResourceManager(path, "r") as file:
            code = file.read().splitlines()
            code = [str.upper(line) for line in code]
            logging.debug(
                "code file loaded: {filename}".format(filename=file.name))
        return code

    @staticmethod
    def read_file(path):
        """ read text file """

        string = ""
        with ResourceManager(path, "r") as file:
            string = file.read()  # read entire file
            logging.debug(
                "text file loaded: {filename}".format(filename=file.name))
        return string

    @staticmethod
    def write(path, content):
        """ write content to file """

        with ResourceManager(path, "w") as file:
            file.write(content)
            logging.debug("wrote file: {filename}".format(filename=file.name))
