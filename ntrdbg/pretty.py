from capstone import *

LINE_FMT = "0x{:08x}:  {}  {}\t{}"
REG_FMT = '''\
r0:  0x{:08x} r1:  0x{:08x} r2:  0x{:08x} r3: 0x{:08x} r4: 0x{:08x}
r5:  0x{:08x} r6:  0x{:08x} r7:  0x{:08x} r8: 0x{:08x} r9: 0x{:08x}
r10: 0x{:08x} r11: 0x{:08x} r12: 0x{:08x}
sp:  0x{:08x} lr:  0x{:08x} pc:  0x{:08x}
'''

md_arm = Cs(CS_ARCH_ARM, CS_MODE_ARM)
md_arm.detail = True

md_thumb = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
md_thumb.detail = True


def print_ins(data, addr, mode, max_count):
  md = None
  if mode == "arm":
    md = md_arm
  elif mode == "thumb":
    md = md_thumb
  else:
    print("unsupported arch")
    return

  count = 0
  for insn in md.disasm(data, addr):
    if count >= max_count:
      break
    print(LINE_FMT.format(insn.address, insn.bytes.hex(),
                          insn.mnemonic, insn.op_str))
    count += 1


def print_ins_arm(data, addr, max_count=10):
  print_ins(data, addr, "arm", max_count)


def print_ins_thumb(data, addr, max_count=10):
  print_ins(data, addr, "thumb", max_count)


def print_regs(regs):
  print(REG_FMT.format(regs["r0"], regs["r1"], regs["r2"], regs["r3"],
                       regs["r4"], regs["r5"], regs["r6"], regs["r7"],
                       regs["r8"], regs["r9"], regs["r10"], regs["r11"],
                       regs["r12"], regs["sp"], regs["lr"], regs["pc"]))
