""" application settings """

import os
import logging
from pathlib import Path
from dotenv import load_dotenv


APP_ROOT = os.path.abspath('.')


class Settings:
    """ Global settings class """

    @staticmethod
    def load():
        """ load global settings.env file """

        env_path = Path(APP_ROOT) / 'settings.env'
        load_dotenv(dotenv_path=env_path, verbose=True)
        logging.basicConfig(level=os.getenv('LOGLEVEL'))
