# Super32 - Designing our own Microprocessor

This repository contains the source code for a simple assembler / compiler for our educational processor.

At the moment this repository consists of two projects. py-assembler is an assembler, written in [Python](https://www.python.org/) and Super32 is an attempt to implement an actuall backend compiler with [LLVM](https://llvm.org/).

Full documentation is found on [readthedocs](super32.readthedocs.io/en/latest).

## Getting Started

These instructions will help you to get your environment ready to build, develop and run the project on your local machine.

### Prerequisites

You'll need the following tools for pyassembler:

- [Python 3](https://www.python.org/)
- Python modules defined in requirements.txt

For the Super32 project you need:

- [LLVM](https://llvm.org/)

### Write assembler code

Take a look at the [instructionset](hhttps://github.com/xsjad0/Super32/blob/master/super32assembler/instructionset.json) of the Super32 processor.
Also, feel free to include [these fancy assembler directives](https://github.com/xsjad0/Super32/blob/master/super32assembler/preprocessor/asmdirectives.py) to improve your code.

Here are some rules you always have to keep in mind when you write some assembler code:

Your code always has to start with
```Assembler
ORG address
START
```
and end with an
```Assembler
END
```
assembler directives, where address MUST be greater than and be able to devide by 4.
Define constants in your memory like this
```Assembler
DEFINE 0
```
For easier referencing the constants in your code, put a lable in front of your constant
```Assembler
const: DEFINE 0
```

### Installation

This python package is currently not available on official PyPi server. To install the package
you first have to clone the git repository

```Bash
git clone https://github.com/xsjad0/Super32.git
```

After you successfully cloned the repository, switch to the latest [release](https://github.com/xsjad0/Super32/releases) and run the installation process via pip

```Bash
git checkout X.Y.Z
pip install .
```

If you do not have pip installed, use the following commands

```Bash
python setup.py build
python setup.py install
```

### Usage

Navigate via cd in the super32assembler folder and provide an assembler code file
via commandline argument.

```Bash
cd super32assembler
python main.py example_code.s32
```

If you want to define a custom output name / path, use the '-o' argument flag.
All available options are listed in the table below.

Option | Default | Description
-|-|-
-h/--help | - | Display help information
-o/--output | \<input-file\>.o | Custom output name / path
-g/--generator | lines | Specify output format. use ```lines``` to generate 32bit machine-code each line. Use ```stream``` to generate one single line machine-code.
-a/--architecture | single | Specify processor architecture. use ```single``` to select single-memory architecture. Use ```multi``` to select dual-memory architecture.

## Running the tests

We use [pytest](https://docs.pytest.org/en/latest/) for testing. To run these test use:

```Bash
pytest test_{test_name}.py
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/xsjad0/Super32/releases).

## Authors

- *Marcel Freiberg* - [freib98](https://github.com/freib98)
- *Marius Schenzle* - [xsjad0](https://github.com/xsjad0)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/xsjad0/Super32/blob/master/LICENSE) file for details

