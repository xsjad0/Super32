import logging
from bitstring import Bits

LOGGER = logging.getLogger('[assembler]')


class Assembler():
    """Assembler class"""

    def __init__(self):
        self.__delimiters = ['(', ')', ',']
        self.__symboltable = {}

    def parse(self, code, commands, registers):
        bitcode = []

        code = self.__generateSymboltable(code)

        for line_nr, line in enumerate(code):
            LOGGER.debug(str(line))
            for delimiter in self.__delimiters:
                line = line.replace(delimiter, ' ')
            line = line.strip()
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
                    self.__parseBranch(
                        line_nr, tokens, commands['branch'], registers)
            else:
                raise Exception(
                    "Parsing error. Command not found: " + tokens[0])

        return bitcode

    def __generateSymboltable(self, code):
        """ builds a dictionary within keys are the lables
        and values are the labels address.
        returns code without labels."""

        code_without_lables = []
        for i, line in enumerate(code):
            label_code = line.split(':')
            label = label_code[0]
            if len(label) != len(line):
                self.__symboltable[label] = i
                instruction = label_code.pop().strip()
                code_without_lables = code_without_lables + [instruction]
            else:
                instruction = label_code.pop().strip()
                code_without_lables = code_without_lables + [instruction]

        return code_without_lables

    def __validateLabel(self, label):
        if label not in self.__symboltable.keys():
            raise Exception("Label not found: " + label)
        else:
            return self.__symboltable.get(label)

    def __validateCodeLength(self, machine_code):
        if len(machine_code) != 32:
            raise Exception('Parsing error')

    def __validateTokenLength(self, tokens):
        if len(tokens) != 4:
            raise Exception('Parsing error')

    def __validateBits(self, machine_code):
        for bit in machine_code:
            if bit not in ['0', '1']:
                raise Exception('Parsing error')

    def __parseArithmetic(self, tokens, arithmetic, registers):
        self.__validateTokenLength(tokens)
        for cmd in arithmetic:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = arithmetic[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        self.__validateBits(''.join(tokens))

        # add 5bit dont-cares and 6bit op-code always zero
        tokens = tokens + ['00000'] + ['000000']

        # rearrenge bit-order
        order = [5, 2, 3, 1, 4, 0]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__validateCodeLength(machine_code)

        LOGGER.debug(machine_code)
        return [machine_code]

    def __parseStorage(self, tokens, storage, registers):
        self.__validateTokenLength(tokens)
        for cmd in storage:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = storage[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        self.__validateBits(''.join(tokens))

        offset = tokens[2]
        tokens[2] = "{:016b}".format(int(offset))

        # rearrenge bit-order
        order = [0, 3, 1, 2]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__validateCodeLength(machine_code)

        LOGGER.debug(machine_code)
        return [machine_code]

    def __parseBranch(self, line_nr, tokens, branch, registers):
        self.__validateTokenLength(tokens)

        if tokens[-1].isdecimal():
            tokens = self.__parseBranchImmediate(tokens, branch, registers)
        else:
            tokens = self.__parseBranchLabel(
                line_nr, tokens, branch, registers)

        self.__validateBits(''.join(tokens))

        # rearrenge bit-order
        order = [0, 2, 1, 3]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__validateCodeLength(machine_code)

        LOGGER.debug(machine_code)
        return [machine_code]

    def __parseBranchImmediate(self, tokens, branch, registers):
        for cmd in branch:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = branch[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        offset = int(tokens[-1])
        tokens[-1] = Bits(int=offset, length=16).bin

        return tokens

    def __parseBranchLabel(self, line_nr, tokens, branch, registers):
        address = self.__validateLabel(tokens[-1])
        for cmd in branch:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = branch[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        # negativ offset indicates to jump backwards
        offset = address - line_nr
        if offset < 0:
            offset -= 1
        tokens[-1] = Bits(int=offset, length=16).bin

        return tokens
