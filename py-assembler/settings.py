import os
import logging
from dotenv import load_dotenv
from pathlib import Path


class Settings:

    @staticmethod
    def load():
        env_path = Path('.') / 'settings.env'
        load_dotenv(dotenv_path=env_path, verbose=True)
        logging.basicConfig(level=os.getenv('LOGLEVEL'))
