from keystone import *
from unicorn import *
from unicorn.x86_const import *

CODE = b"mov rax, 1111;mov rdx, rax;add rax, rax;add rax, rdx"

ADDRESS = 0x1000000

ue = Uc(UC_ARCH_X86, UC_MODE_64)
ue.mem_map(0x1000000, 4 * 1024 * 1024)

ks = Ks(KS_ARCH_X86, KS_MODE_64)
bytecode, count = ks.asm(CODE, as_bytes=True)

ue.mem_write(ADDRESS, bytecode)
ue.emu_start(ADDRESS, ADDRESS + len(bytecode))

rax = ue.reg_read(UC_X86_REG_RAX)

print("RAX = %d" % rax)