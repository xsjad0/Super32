""" python assembler """

import argparse
from pyassembler.inout.fileio import FileIO
from pyassembler.assembler.assembler import Assembler
from pyassembler.settings.settings import Settings
from pyassembler.generator.generator import Generator


def main(args):
    """ main entry point for python Super32 assembler """

    Settings.load()
    cfg = FileIO.read_json('instructionset.json')
    code = FileIO.read_code(args.input)

    assembler = Assembler()
    generator = Generator(args.generator)

    machine_code = assembler.parse(
        code, commands=cfg['commands'], registers=cfg['registers'])

    generator.write(args.output, machine_code)


if __name__ == "__main__":
    ARGPARSER = argparse.ArgumentParser(description='Super32 assembly parser')
    ARGPARSER.add_argument('input',
                           help='path to assembler file')
    ARGPARSER.add_argument('-g', '--generator', choices=['stream', 'lines'], default='lines',
                           metavar='generator', help='specify output format')
    ARGPARSER.add_argument('-o', '--output', metavar='output',
                           help='path to generated machinecode file')
    ARGS = ARGPARSER.parse_args()

    if ARGS.output is None:
        ARGS.output = ARGS.input.rsplit('.', 1)[0] + '.o'

    main(ARGS)
