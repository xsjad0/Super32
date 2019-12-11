"""
Preprocessor Module
"""

import logging
from bitstring import Bits
from .asmdirectives import AssemblerDirectives

REG_SIZE = 4  # bytes
ZEROS = "{:032b}".format(0)


class Preprocessor:
    def __init__(self):
        pass

    def parse(self, input_file):

        # trim and filter empty lines
        input_file = [str.strip(line) for line in input_file if line]

        # generate storage dump with zeros from first to last address
        zeros = self.__generate_zeros(input_file)

        # parse assembler directives, insert constants
        # and search codes startaddress
        code_address, zeros_constants = self.__parse_assembler_directives(
            input_file, zeros)

        # filter assembler code
        code = self.__filter_code(input_file)

        return code_address, code, zeros_constants

    def __parse_assembler_directives(self, input_file, zeros):
        zeros_constants = zeros[:]
        address = 0
        code_address = 0
        org = False
        start, end = False, False
        for line in input_file:
            tokens = line.split(' ')
            asm_directive = tokens[0]
            if tokens[0] in AssemblerDirectives.to_string():
                if asm_directive == AssemblerDirectives.ORG.name:
                    address = int(tokens[1])
                    org = True
                elif asm_directive == AssemblerDirectives.DEFINE.name:
                    constant = int(tokens[1])
                    constant_bin = Bits(int=constant, length=32).bin
                    index = int(address / REG_SIZE)
                    zeros_constants[index] = constant_bin
                    address = address + REG_SIZE
                    org = False
                elif asm_directive == AssemblerDirectives.START.name:
                    if org:
                        start = True
                        code_address = address
                elif asm_directive == AssemblerDirectives.END.name:
                    end = True
                else:
                    pass  # assembler code

        if not start or not end:
            raise Exception(
                'Preprocessor error. Missing START- and/or END-directive')
        return code_address, zeros_constants

    def __generate_zeros(self, input_file):
        org_found = False
        max_address = 0
        for line in input_file:  # seach for maximum address
            tokens = line.split(' ')
            if tokens[0] == AssemblerDirectives.ORG.name:
                max_address = int(tokens[1])
                org_found = True
            elif not tokens[0] == AssemblerDirectives.START.name and not tokens[0] == AssemblerDirectives.END.name:
                max_address = max_address + REG_SIZE

        if not org_found:
            raise Exception('Code have to start with ORG-directive')

        return [ZEROS for address in range(
            0,
            max_address
        ) if not address % REG_SIZE]

    def __filter_code(self, input_file):
        start_index, end_index = 0, 0
        start_index = input_file.index(
            AssemblerDirectives.START.name) + 1
        end_index = input_file.index(AssemblerDirectives.END.name)

        return input_file[start_index:end_index]
