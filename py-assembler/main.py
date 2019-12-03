# python assembler
import argparse
import logging
import json
import sys
import os
from resource_manager import ResourceManager
from fileio import FileIO
from assembler import Assembler
from settings import Settings


def main(args):
    Settings.load()
    cfg = FileIO.read_json('config.json')
    code = FileIO.read_code(args.input)

    assembler = Assembler()
    machine_code = assembler.parse(
        code, commands=cfg['commands'], registers=cfg['registers'])

    with ResourceManager(args.output, 'w') as output_file:
        output_file.write(machine_code)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Super32 assembly parser')
    argparser.add_argument('input',
                           help='path to assembler file')
    argparser.add_argument('-o', '--output', metavar='output-file',
                           help='path to generated machinecode file')
    args = argparser.parse_args()

    if (args.output == None):
        args.output = args.input.rsplit('.', 1)[0] + '.o'

    main(args)
