//===- Super32InstrInfo.td - Target Description for Super32 Target -*- tablegen -*-=//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//
//
// This file contains the Super32 implementation of the TargetInstrInfo class.
//
//===----------------------------------------------------------------------===//


//===----------------------------------------------------------------------===//
// Instruction format superclass
//===----------------------------------------------------------------------===//

include "Super32InstrFormats.td"

//===----------------------------------------------------------------------===//
// Instructions specific format
//===----------------------------------------------------------------------===//

class ArithLogicI<bits<6> op, string instr_asm, RegisterClass RC> :
  FL<op, (outs GPROut:$ra), (ins RC:$rb, RC:$rc),
     !strconcat(instr_asm, "\t$r0, $r1, $r2")> {
  let isReMaterializable = 1;
}


//===----------------------------------------------------------------------===//
// Instruction definition
//===----------------------------------------------------------------------===//

//===----------------------------------------------------------------------===//
// Super32 Instructions
//===----------------------------------------------------------------------===//

/// Load and Store Instructions
///  aligned
// defm LD     : LoadM32<0x01,  "ld",  load_a>;
// defm ST     : StoreM32<0x02, "st",  store_a>;

/// Arithmetic Instructions
def ADD   : ArithLogicI<0x01, "add", CPURegs>;
def SUB   : ArithLogicI<0x02, "sub", CPURegs>;
