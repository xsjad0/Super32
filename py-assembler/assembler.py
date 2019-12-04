import logging

logger = logging.getLogger('[assembler]')


class Assembler():
    """Assembler class"""

    def __init__(self):
        self.delimiters = ['(', ')', ',']

    def parse(self, code, commands, registers):
        bitcode = []
        for line in code:
            logger.debug(str(line))
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
                raise Exception(
                    "Parsing error. Command not found: " + tokens[0])

        return bitcode

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

        logger.debug(machine_code)
        return [machine_code]

    def __parseStorage(self, tokens, storage, registers):
        tokens = tokens[:-1]
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

        logger.debug(machine_code)
        return [machine_code]

    def __parseBranch(self, tokens, branch, registers):
        self.__validateTokenLength(tokens)
        for cmd in branch:
            for i, token in enumerate(tokens):
                if token == cmd:
                    tokens[i] = branch[cmd]
                    break

        for reg in registers:
            for i, token in enumerate(tokens):
                if token == reg:
                    tokens[i] = registers[reg]

        self.__validateBits(''.join(tokens))

        offset = tokens[3]
        tokens[3] = "{:016b}".format(int(offset))

        # rearrenge bit-order
        order = [0, 2, 1, 3]
        tokens = [tokens[i] for i in order]

        machine_code = ''.join(tokens)
        self.__validateCodeLength(machine_code)

        logger.debug(machine_code)
        return [machine_code]
