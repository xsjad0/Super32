# python assembler
import logging
import json
import sys
import os
from resource_manager import ResourceManager
from fileio import FileIO
from assembler import Assembler

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger("[assembler]")


def main(args):
    cfg = FileIO.read_json('config.json')
    code = FileIO.read_code(args[0])

    assembler = Assembler()
    machine_code = assembler.parse(
        code, commands=cfg['commands'], registers=cfg['registers'])

    with ResourceManager(args[1], 'w') as output_file:
        output_file.write(machine_code)


if __name__ == "__main__":
    main(sys.argv[1:])
