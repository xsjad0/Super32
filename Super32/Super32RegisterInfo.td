//===-- Super32RegisterInfo.td - Super32 Register defs -----------*- tablegen -*-===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//

//===----------------------------------------------------------------------===//
//  Declarations that describe the Super32 register file
//===----------------------------------------------------------------------===//

// We have banks of 16 registers each.
class Super32Reg<bits<16> Enc, string n> : Register<n> {
  // For tablegen(... -gen-emitter)  in CMakeLists.txt
  let HWEncoding = Enc;
  let Namespace = "Super32";
}

// Super32 CPU Registers
class Super32GPRReg<bits<16> Enc, string n> : Super32Reg<Enc, n>;

// Co-processor 0 Registers
class Super32C0Reg<bits<16> Enc, string n> : Super32Reg<Enc, n>;

//===----------------------------------------------------------------------===//
//@Registers
//===----------------------------------------------------------------------===//
// The register string, such as "9" or "gp" will show on "llvm-objdump -d"
//@ All registers definition
let Namespace = "Super32" in {
  //@ General Purpose Registers
  def R0    : Super32GPRReg<0,  "r0">,    DwarfRegNum<[0]>;
  def R1    : Super32GPRReg<1,  "r1">,    DwarfRegNum<[1]>;
  def R2    : Super32GPRReg<2,  "r2">,    DwarfRegNum<[2]>;
  def R3    : Super32GPRReg<3,  "r3">,    DwarfRegNum<[3]>;
  def R4    : Super32GPRReg<4,  "r4">,    DwarfRegNum<[4]>;
  def R5    : Super32GPRReg<5,  "r5">,    DwarfRegNum<[5]>;
  def R6    : Super32GPRReg<6,  "r6">,    DwarfRegNum<[6]>;
  def R7    : Super32GPRReg<7,  "r7">,    DwarfRegNum<[7]>;
  def R8    : Super32GPRReg<8,  "r8">,    DwarfRegNum<[8]>;
  def R9    : Super32GPRReg<9,  "r9">,    DwarfRegNum<[9]>;
  def R10   : Super32GPRReg<10, "r10">,   DwarfRegNum<[10]>;
  def R11   : Super32GPRReg<11, "r11">,   DwarfRegNum<[11]>;
  def R12   : Super32GPRReg<12, "r12">,   DwarfRegNum<[12]>;
  def R13   : Super32GPRReg<13, "r13">,   DwarfRegNum<[13]>;
  def R14   : Super32GPRReg<14, "r14">,   DwarfRegNum<[14]>;
  def R15   : Super32GPRReg<15, "r15">,   DwarfRegNum<[15]>;

  def PC   : Super32C0Reg<0, "pc">,  DwarfRegNum<[16]>;
  def EPC   : Super32C0Reg<0, "epc">,  DwarfRegNum<[17]>;
}

//===----------------------------------------------------------------------===//
//@Register Classes
//===----------------------------------------------------------------------===//

def CPURegs : RegisterClass<"Super32", [i32], 32, (add
  R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15)>;

//@Co-processor 0 Registers class
def C0Regs : RegisterClass<"Super32", [i32], 32, (add PC)>;

// offer GPROut for other use
def GPROut : RegisterClass<"Super32", [i32], 32, (add (sub CPURegs, EPC))>;
