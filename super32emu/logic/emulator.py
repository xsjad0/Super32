"""Emulator-Logic"""
from super32assembler.assembler.assembler import Assembler
from super32assembler.preprocessor.preprocessor import Preprocessor
from super32assembler.assembler.architecture import Architectures
from super32utils.inout.fileio import FileIO
from bitstring import BitArray


class Emulator():
    """This is the logic to emulate the assembly instructions"""

    def __init__(self, editor_widget, emulator_widget, footer_widget):
        self.editor_widget = editor_widget
        self.emulator_widget = emulator_widget
        self.footer_widget = footer_widget

        for rindex in range(32):
            self.emulator_widget.set_register(rindex, '0000')

        self.emulator_widget.set_pc(0)
        self.emulator_widget.set_storage(''.ljust(2**10, '0'))
        self.emulator_widget.set_symbols({"-": "-"})

        self.cfg = FileIO.read_json('instructionset.json')
        self.commands = self.cfg['commands']
        self.memory = []

    def run(self):
        """Parse and execute the commands written in the editor"""

        preprocessor = Preprocessor()
        assembler = Assembler(Architectures.SINGLE)

        code_address, code, zeros_constants, symboltable = preprocessor.parse(
            input_file=self.editor_widget.get_text()
        )
        self.memory = assembler.parse(
            code_address=code_address,
            code=code,
            zeros_constants=zeros_constants,
            commands=self.cfg['commands'],
            registers=self.cfg['registers'],
            symboltable=symboltable
        )
        self.emulator_widget.set_symbols(symboltable)

        self.__emulate()

    def __emulate(self):
        self.emulator_widget.set_storage(
            ''.join(self.memory).ljust(2**10, '0'))

        address_counter = 0
        self.row_counter = 0

        while self.row_counter < len(self.memory):
            instructionset = self.memory[self.row_counter]

            instruction = instructionset[0:6]

            if instruction == '000000':
                self.__arithmetic_instruction(
                    instructionset[6:11],
                    instructionset[11:16],
                    instructionset[16:21],
                    instructionset[26:32])
            elif instruction == self.commands['branch']['BEQ']:
                self.__branch(
                    instructionset[6:11],
                    instructionset[11:16],
                    instructionset[16:32])
            elif instruction == self.commands['storage']['LW']:
                self.__load(
                    instructionset[6:11],
                    instructionset[11:16],
                    instructionset[16:32])
            elif instruction == self.commands['storage']['SW']:
                self.__save(
                    instructionset[6:11],
                    instructionset[11:16],
                    instructionset[16:31])

            self.row_counter += 1
            address_counter = self.row_counter * 4

            self.emulator_widget.set_pc(address_counter)
            self.emulator_widget.set_storage(
                ''.join(self.memory).ljust(2**10, '0'))

    def __arithmetic_instruction(self, first_source, second_source, target, func):
        if func == self.commands['arithmetic']['SUB']:
            result = bin(int(first_source) - int(second_source))
            register = self.__get_register(target)
            self.emulator_widget.set_register(register, result)
        elif func == self.commands['arithmetic']['ADD']:
            result = bin(int(first_source) + int(second_source))
            register = self.__get_register(target)
            self.emulator_widget.set_register(register, result)
        elif func == self.commands['arithmetic']['AND']:
            result = bin(int(first_source) & int(second_source))
            self.emulator_widget.set_register(0, result)
        elif func == self.commands['arithmetic']['OR']:
            result = bin(int(first_source) | int(second_source))
            self.emulator_widget.set_register(0, result)
        elif func == self.commands['arithmetic']['NOR']:
            result = bin(int(first_source) | int(second_source)
                         ^ 0b11111111)
            self.emulator_widget.set_register(0, result)

    def __branch(self, r2, r1, offset):
        if r2 == r1:
            offset = BitArray(bin=offset).int
            self.row_counter + offset - 1

    def __load(self, r2, r1, offset):
        offset = BitArray(bin=offset).int
        r2 = BitArray(bin=r2).int
        address = offset + r2
        r1 = self.memory[address]

    def __save(self, r2, r1, offset):
        offset = BitArray(bin=offset).int
        r2 = BitArray(bin=r2).int
        address = offset + r2
        self.memory[address] = r1

    def __get_register(self, target):
        for register in self.cfg['registers']:
            value = self.cfg['registers'][register]
            if target == value:
                return int(value, 2)
