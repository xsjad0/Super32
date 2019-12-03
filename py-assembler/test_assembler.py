import pytest
import json

from assembler import Assembler


jsonString = u'{"commands": { "arithmetic": { "SUB": "000110", "ADD": "000010", "AND": "000000", "OR": "000001", "NOR": "001100" }, "branch": { "BEQ": "000100" }, "storage": { "LW": "100011", "SW": "101011" } }, "registers": { "R0": "00000", "R1": "00001", "R2": "00010", "R3": "00011", "R4": "00100", "R5": "00101", "R6": "00110", "R7": "00111", "R8": "01000", "R9": "01001", "R10": "01010", "R11": "01011", "R12": "01100", "R13": "01101", "R14": "01110", "R15": "01111", "R16": "10000", "R17": "10001", "R18": "10010", "R19": "10011", "R20": "10100", "R21": "10101", "R22": "10110", "R23": "10111", "R24": "11000", "R25": "11001", "R26": "11010", "R27": "11011", "R28": "11100", "R29": "11101", "R30": "11110", "R31": "11111" }}'
cfg = json.loads(jsonString)
assembler = Assembler()


def test_parse_add():
    result = assembler.parse(
        ['ADD R1,R20,R12'], commands=cfg['commands'], registers=cfg['registers'])

    assert result == "00000010100011000000100000000010"


def test_parse_sub():
    result = assembler.parse(
        ['SUB R2,R1,R4'], commands=cfg['commands'], registers=cfg['registers'])

    assert result == "00000000001001000001000000000110"


def test_parse_lw():
    result = assembler.parse(
        ['LW R1,0(R2)'], commands=cfg['commands'], registers=cfg['registers'])

    assert result == "10001100010000010000000000000000"


def test_parse_sw():
    result = assembler.parse(
        ['SW R1,0(R2)'], commands=cfg['commands'], registers=cfg['registers'])

    assert result == "10101100010000010000000000000000"


def test_parse_beq():
    result = assembler.parse(
        ['BEQ R1,R2,0'], commands=cfg['commands'], registers=cfg['registers'])

    assert result == "00010000010000010000000000000000"
