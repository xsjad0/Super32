""" assembler tests """
import json
import pytest

from super32assembler.assembler.assembler import Assembler
from super32assembler.assembler.architecture import Architectures
from super32assembler.preprocessor.preprocessor import Preprocessor


JSON_STRING = (
    '{"commands": { "arithmetic":'
    '{"SUB": "000010", "ADD": "000000", "AND": "000100", "OR": "000101", "NOR": "001010"}'
    ', "branch": { "BEQ": "000100" }, "storage": { "LW": "100011", "SW": "101011" } }'
    ', "registers": { "R0": "00000", "R1": "00001", "R2": "00010", "R3": "00011", '
    '"R4": "00100", "R5": "00101", "R6": "00110", "R7": "00111", "R8": "01000", '
    '"R9": "01001", "R10": "01010", "R11": "01011", "R12": "01100", "R13": "01101", '
    '"R14": "01110", "R15": "01111", "R16": "10000", "R17": "10001", "R18": "10010",'
    '"R19": "10011", "R20": "10100", "R21": "10101", "R22": "10110", "R23": "10111",'
    '"R24": "11000", "R25": "11001", "R26": "11010", "R27": "11011", "R28": "11100",'
    '"R29": "11101", "R30": "11110", "R31": "11111"}}'
)
CFG = json.loads(JSON_STRING)
ASSEMBLER = Assembler(Architectures.SINGLE)
PREPROCESSOR = Preprocessor()


def test_parse_add():
    fake_input_file = ['ORG 4', 'START', 'ADD R1,R20,R12', 'END']
    code_address, code, zeros_constants, symboltable = PREPROCESSOR.parse(
        fake_input_file)
    result = ASSEMBLER.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=CFG['commands'],
        registers=CFG['registers'],
        symboltable=symboltable
    )

    assert result == [
        '00010000010000010000000000000000',
        '00000010100011000000100000000000'
    ]


def test_parse_sub():
    fake_input_file = ['ORG 4', 'START', 'SUB R2,R1,R4', 'END']
    code_address, code, zeros_constants, symboltable = PREPROCESSOR.parse(
        fake_input_file)
    result = ASSEMBLER.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=CFG['commands'],
        registers=CFG['registers'],
        symboltable=symboltable
    )

    assert result == [
        '00010000010000010000000000000000',
        '00000000001001000001000000000010'
    ]


def test_parse_lw():
    fake_input_file = ['ORG 4', 'START', 'LW R1,0(R2)', 'END']
    code_address, code, zeros_constants, symboltable = PREPROCESSOR.parse(
        fake_input_file)
    result = ASSEMBLER.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=CFG['commands'],
        registers=CFG['registers'],
        symboltable=symboltable
    )

    assert result == [
        '00010000010000010000000000000000',
        '10001100010000010000000000000000'
    ]


def test_parse_sw():
    fake_input_file = ['ORG 4', 'START', 'SW R1,0(R2)', 'END']
    code_address, code, zeros_constants, symboltable = PREPROCESSOR.parse(
        fake_input_file)
    result = ASSEMBLER.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=CFG['commands'],
        registers=CFG['registers'],
        symboltable=symboltable
    )

    assert result == [
        '00010000010000010000000000000000',
        '10101100010000010000000000000000'
    ]


def test_parse_beq_imm():
    fake_input_file = ['ORG 4', 'START', 'BEQ R1,R2,0', 'END']
    code_address, code, zeros_constants, symboltable = PREPROCESSOR.parse(
        fake_input_file)
    result = ASSEMBLER.parse(
        code_address=code_address,
        code=code,
        zeros_constants=zeros_constants,
        commands=CFG['commands'],
        registers=CFG['registers'],
        symboltable=symboltable
    )

    assert result == [
        '00010000010000010000000000000000',
        '00010000010000010000000000000000'
    ]


def test_parse_beq_label():
    # TODO: Test parse branch with label
    pass
