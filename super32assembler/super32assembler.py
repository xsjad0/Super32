"""
Usage:
    super32assembler parse [--output=path]
                           [--architecture=single | --architecture=multi]
                           [--generator=lines | --generator=stream] <input-file>
    super32assembler (-h | --help)


Options:
    -h --help               show this screen and exit
    --output=<path>         specify the generated output file
    --architecture=<type>   specify processor architecture [default: single]
    --generator=<type>      specify output file format [default: lines]
"""

from docopt import docopt
from super32utils.inout.fileio import FileIO
from super32utils.settings.settings import Settings
from assembler.assembler import Assembler
from assembler.architecture import Architectures
from generator.generator import Generator
from preprocessor.preprocessor import Preprocessor


def single(ARGS):
    """ main entry point for python Super32 assembler
    (with single storage)
    """

    Settings.load()
    cfg = FileIO.read_json('instructionset.json')
    input_file = FileIO.read_code(ARGS['<input-file>'])

    preprocessor = Preprocessor()
    assembler = Assembler(Architectures.SINGLE)
    generator = Generator(ARGS['--generator'])

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

    generator.write(ARGS['--output'], machine_code)


def multi(ARGS):
    """ main entry point for python Super32 assembler
    (with separate storages for instructions and data)
    """

    Settings.load()
    cfg = FileIO.read_json('instructionset.json')
    input_file = FileIO.read_code(ARGS['<input-file>'])

    preprocessor = Preprocessor()
    assembler = Assembler(Architectures.MULTI)
    generator = Generator(ARGS['--generator'])

    code_address, code, zeros_constants, symboltable = preprocessor.parse(
        input_file=input_file
    )

    machine_code_instructions = assembler.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=cfg['commands'],
        registers=cfg['registers'],
        symboltable=symboltable
    )

    generator.write(ARGS['--output'][0], machine_code_instructions)
    generator.write(ARGS['--output'][1], zeros_constants)


if __name__ == "__main__":
    ARGS = docopt(__doc__)

    if ARGS['--output'] is None:
        ARGS['--output'] = ARGS['<input-file>'].rsplit('.', 1)[0] + '.o'

    # choose super32 architecture
    if ARGS['--architecture'] == 'multi':
        OUTPUT = ARGS['--output'].rsplit('.')
        NAME = OUTPUT[0]
        ENDING = OUTPUT[-1]
        ARGS['--output'] = [
            "{filename}_{extension}.{fileending}".format(
                filename=NAME,
                extension='instructions',
                fileending=ENDING
            ),
            "{filename}_{extension}.{fileending}".format(
                filename=NAME,
                extension='memory',
                fileending=ENDING
            )
        ]
        multi(ARGS)
    else:
        single(ARGS)
