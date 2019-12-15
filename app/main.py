""" python assembler """

import argparse
from pyassembler.inout.fileio import FileIO
from pyassembler.assembler.assembler import Assembler
from pyassembler.settings.settings import Settings
from pyassembler.generator.generator import Generator
from pyassembler.preprocessor.preprocessor import Preprocessor
from pyassembler.assembler.architecture import Architectures


def single(args):
    """ main entry point for python Super32 assembler 
    (with single storage)
    """

    Settings.load()
    cfg = FileIO.read_json('instructionset.json')
    input_file = FileIO.read_code(args.input)

    preprocessor = Preprocessor()
    assembler = Assembler(Architectures.SINGLE)
    generator = Generator(args.generator)

    code_address, code, zeros_constants, symboltable = preprocessor.parse(
        input_file=input_file
    )
    machine_code = assembler.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=cfg['commands'],
        registers=cfg['registers'],
        symboltable=symboltable
    )

    generator.write(args.output, machine_code)


def multi(args):
    """ main entry point for python Super32 assembler 
    (with separate storages for instructions and data)
    """

    Settings.load()
    cfg = FileIO.read_json('instructionset.json')
    input_file = FileIO.read_code(args.input)

    preprocessor = Preprocessor()
    assembler = Assembler(Architectures.MULTI)
    generator = Generator(args.generator)

    code_address, code, zeros_constants = preprocessor.parse(
        input_file=input_file
    )

    machine_code_instructions = assembler.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=cfg['commands'],
        registers=cfg['registers']
    )

    generator.write(args.output[0], machine_code_instructions)
    generator.write(args.output[1], zeros_constants)


if __name__ == "__main__":
    ARGPARSER = argparse.ArgumentParser(description='Super32 assembly parser')
    ARGPARSER.add_argument(
        'input',
        help='path to assembler file'
    )
    ARGPARSER.add_argument(
        '-g', '--generator',
        choices=['stream', 'lines'],
        default='lines',
        metavar='generator',
        help='specify output format'
    )
    ARGPARSER.add_argument(
        '-a', '--architecture',
        choices=['single', 'multi'],
        default='single',
        metavar='architecture',
        help='specify processor architecture'
    )
    ARGPARSER.add_argument(
        '-o', '--output',
        default='output',
        metavar='output',
        help='path to generated machinecode file'
    )
    ARGS = ARGPARSER.parse_args()

    # choose super32 architecture
    if ARGS.architecture == 'multi':
        ARGS.output = [
            ARGS.output + '_instructions.txt',
            ARGS.output + '_constants.txt'
        ]
        multi(ARGS)
    else:
        ARGS.output = ARGS.output + '.txt'
        single(ARGS)
