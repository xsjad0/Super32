# Super32 - Designing our own Microprocessor

This repository contains the source code for a simple assembler / compiler for our educational processor.

At the moment this repository consists of two projects. py-assembler is an assembler, written in [Python](https://www.python.org/) and Super32 is an attempt to implement an actuall backend compiler with [LLVM](https://llvm.org/).

## Getting Started

These instructions will help you to get your environment ready to build, develop and run the project on your local machine.

### Prerequisites

You'll need the following tools for py-assembler:

- [Python 3](https://www.python.org/)
- Python modules defined in requirements.txt

For the Super32 project you need:

- [LLVM](https://llvm.org/)

### Run py-assembler

To use the python assembler you must change directory to py-assembler and run main.py with python. To actually assemble code you have to provide an input file via argument.

```Bash
cd py-assembler
python main.py input.txt
```

If you want to define a custom output name / path, use the '-o' argument flag.

## Running the tests

We use [pytest](https://docs.pytest.org/en/latest/) for testing. To run these test use:

```Bash
pytest test_{test_name}.py
```
