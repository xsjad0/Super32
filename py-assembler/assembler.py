# python assembler
import logging
import json
import sys
import os
from resource_manager import ResourceManager
from fileio import FileIO

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger("[assembler]")


class Parser():
    def __init__(self):
        pass

    def parse(self, code, commands, registers):
        bitcode = []
        for line in code:
            if line == '\n':
                continue
            elif line.split(' ')[0] in commands['arithmetic']:
                bitcode = bitcode + self.__parseArithmetic(
                    line, commands['arithmetic'], registers)
            elif line.split(' ')[0] in commands['storage']:
                bitcode = bitcode + self.__parseStorage(
                    line, commands['storage'], registers)
            elif line.split(' ')[0] in commands['branch']:
                bitcode = bitcode + \
                    self.__parseBranch(line, commands['branch'], registers)
            else:
                raise Exception("parse error command")

        return ''.join(bitcode)

    def __checkLine(self, line):
        if len(line) != 32:
            raise Exception('Parsing error')

        for bit in line:
            if bit not in [0, 1]:
                raise Exception('Parsing error')

    def __parseArithmetic(self, line, arithmetic, registers):
        for cmd in arithmetic:
            line = line.replace(cmd, arithmetic[cmd])

        for reg in registers:
            if (reg + '\n') in line:
                line = line.replace((reg + '\n'), registers[reg])
            elif (reg + ',') in line:
                line = line.replace((reg + ','), registers[reg])

        if ' ' in line:
            line = line.replace(' ', '')

        # self.__checkLine(line)

        return [line]

    def __parseStorage(self, line, storage, registers):
        for cmd in storage:
            line = line.replace(cmd, storage[cmd])

        for reg in registers:
            if ('(' + reg + ')\n') in line:
                line = line.replace(('(' + reg + ')\n'), registers[reg])
            elif (reg + ',') in line:
                line = line.replace((reg + ','), registers[reg])

        if ' ' in line:
            line = line.replace(' ', '')

        # self.__checkLine(line)

        return [line]

    def __parseBranch(self, line, branch, registers):
        for cmd in branch:
            line = line.replace(cmd, branch[cmd])

        offset = line.split(',')[-1]
        line = line.replace(offset, '{:016b}'.format(int(offset)))

        for reg in registers:
            if (reg + ',') in line:
                line = line.replace((reg + ','), registers[reg])

        if ' ' in line:
            line = line.replace(' ', '')

        # self.__checkLine(line)

        return [line]


def main(args):
    cfg = FileIO.read_json('config.json')
    code = FileIO.read_code(args[0])

    parser = Parser()
    machine_code = parser.parse(
        code, commands=cfg['commands'], registers=cfg['registers'])

    with ResourceManager(args[1], 'w') as output_file:
        output_file.write(machine_code)


if __name__ == "__main__":
    main(sys.argv[1:])
