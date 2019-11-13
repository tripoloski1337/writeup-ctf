from pwn import *
import string
import binascii
import re
'''
Please give me the 01110010 01101111 01100010 01101111 01110100 as a word. //bin
To make things interesting, you have 30 seconds.
Input:
robot
Please give me the 73746f7665 as a word. // hex
Input:
stove
Please give me the  160 154 165 147 as a word. // octal
'''
def decode_binary_string(s):
	return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def decode(p,ln):
	msg = ""
	print ln[0]
	if len(ln[0]) == 8 and "a" not in p and "b" not in p and "c" not in p and "d" not in p and "e" not in p and "f" not in p : # Convert binary
		msg += decode_binary_string(p)
	elif len(ln[0]) == "3": # Convert octal (ciri2 octal adalah awalnya merupakan angka 0
		msg += chr(int(p, 8))
	elif len(p) == 3 and p[0] != '0' : # Convert decimal
		msg += chr(int(p))
	elif len(re.findall(r"[a-z]", p)) > 0 or "a" in p or "b" in p or "c" in p or "d" in p or "e" in p or "f" in p: # Convert hexadecimal
		msg += binascii.unhexlify(p)
	elif len(p[1]) == "3":	
		msg += chr(int(p,10))
	else:
		log.info("octal : " + str(p))
		for i in ln:
			msg += chr(int(i, 8))
	print msg
	return msg

def main():
	r = remote("2018shell.picoctf.com",31711)
	
	for i in range(100):
		plaintext = ''
		r.recvuntil('Please give me the ')
		raw = r.recvline().replace('as a word.\n','')
		res = raw.replace(' ','')
		ln = raw.split()
		log.info("receive : " + raw)
		plaintext = decode(res,ln)
		log.info("length : " + str(ln))
		log.info("translating as : " + str(plaintext))
		log.info("sending..")
		r.sendline(plaintext)
		if i == 2:
			r.interactive()


if __name__ == '__main__':
	main()