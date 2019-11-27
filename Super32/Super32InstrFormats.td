//===-- Cpu0InstrFormats.td - Cpu0 Instruction Formats -----*- tablegen -*-===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//

//===----------------------------------------------------------------------===//
//  Describe CPU0 instructions format
//
//  CPU INSTRUCTION FORMATS
//
//  opcode  - operation code.
//  ra      - dst reg, only used on 3 regs instr.
//  rb      - src reg.
//  rc      - src reg (on a 3 reg instr).
//  cx      - immediate
//
//===----------------------------------------------------------------------===//


// Generic Cpu0 Format
class Cpu0Inst<dag outs, dag ins, string asmstr> : Instruction
{
  field bits<32> Inst;

  let Namespace = "Super32";

  let Size = 4;

  bits<6> Opcode = 0;

  // Top 5 bits are the 'opcode' field
  let Inst{31-26} = Opcode;

  let OutOperandList = outs;
  let InOperandList  = ins;

  let AsmString   = asmstr;

  let DecoderNamespace = "Super32";

}

//@class FL {
//===----------------------------------------------------------------------===//
// Format L instruction class in Cpu0 : <|opcode|ra|rb|rc|dc|alu|>
//===----------------------------------------------------------------------===//

class FL<bits<6> op, dag outs, dag ins, string asmstr>
  : Cpu0Inst<outs, ins, asmstr>
{
  bits<5> ra;
  bits<5> rb;
  bits<5> rc;
  bits<5> dc;
  bits<6> alu;
  
  let Opcode = op;

  let Inst{25-21} = ra;
  let Inst{20-16} = rb;
  let Inst{15-11} = rc;
  let Inst{10-6}  = dc;
  let Inst{5-0}   = alu;
}