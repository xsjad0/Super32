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
        self.delimiters = ['(', ')', ',']

    def parse(self, code, commands, registers):
        bitcode = []
        for line in code:
            for delimiter in self.delimiters:
                line = line.replace(delimiter, ' ')
            tokens = line.split(' ')
            if len(tokens[0]) == 0:
                continue
            elif tokens[0] in commands['arithmetic']:
                bitcode = bitcode + self.__parseArithmetic(
                    tokens, commands['arithmetic'], registers)
            elif tokens[0] in commands['storage']:
                bitcode = bitcode + self.__parseStorage(
                    tokens, commands['storage'], registers)
            elif tokens[0] in commands['branch']:
                bitcode = bitcode + \
                    self.__parseBranch(tokens, commands['branch'], registers)
            else:
                raise Exception("parse error command")

        return ''.join(bitcode)

    def __checkLine(self, machine_code):
        if len(machine_code) != 32:
            raise Exception('Parsing error')

        for bit in machine_code:
            if bit not in ['0', '1']:
                raise Exception('Parsing error')

    def __parseArithmetic(self, tokens, arithmetic, registers):
        for cmd in arithmetic:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = arithmetic[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        # add 5bit dont-cares and 6bit op-code always zero
        tokens = tokens + ['00000'] + ['000000']

        # rearrenge bit-order
        order = [5, 2, 3, 1, 4, 0]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__checkLine(machine_code)

        return [machine_code]

    def __parseStorage(self, tokens, storage, registers):
        tokens = tokens[:-1]
        for cmd in storage:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = storage[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        offset = tokens[2]
        tokens[2] = "{:016b}".format(int(offset))

        # rearrenge bit-order
        order = [0, 3, 1, 2]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__checkLine(machine_code)

        return [machine_code]

    def __parseBranch(self, tokens, branch, registers):
        for cmd in branch:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = branch[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        offset = tokens[3]
        tokens[3] = "{:016b}".format(int(offset))

        # rearrenge bit-order
        order = [0, 2, 1, 3]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__checkLine(machine_code)

        return [machine_code]


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
