class ResourceManager(object):
    """Context manager class to handle system ressources"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.open_file = open(self.filename, self.mode)
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
