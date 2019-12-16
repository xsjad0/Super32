""" File format generator module """

from super32utils.inout.fileio import FileIO


class Generator:
    """ Format machinecode output """

    def __init__(self, generator):
        self.__generator = generator

    def write(self, path, machine_code):
        if self.__generator == 'stream':
            self.__write_stream(path, machine_code)
        elif self.__generator == 'lines':
            self.__write_lines(path, machine_code)
        else:
            raise Exception('Generator error')

    def __write_stream(self, path, machine_code):
        FileIO.write(path, ''.join(machine_code))

    def __write_lines(self, path, machine_code):
        FileIO.write(path, '\n'.join(machine_code))
