from pwn import *
def getToken():
    x = ''
    x += '1F6D1F1D191E6E6E'.decode('hex')[::-1]
    x += '6E20421B1E1F206B'.decode('hex')[::-1]
    x += '6A201A6F411E1E6E'.decode('hex')[::-1]
    x += '6C1C6C1C6C1D6C6D'.decode('hex')[::-1]

    # a1[i] = ((a1[i] + 8) ^ 0x10) - 15;
    p = ''
    for i in x:
        p += chr(((ord(i) + 15) ^ 0x10) - 8)

    return p


def main():
    tok = getToken()
    while True:
        r = remote("tasks.aeroctf.com",44324)
        r.recvuntil("Enter valid token to binary with name ")
        x = r.recv(34)
        x = x.replace("<",'').replace('>','')
        if x == 'ffeabd223de0d4eacb9a3e6e53e5448d':
            r.sendline(tok)
            r.interactive()
            break
        # print r.recvline()
        r.close()
        # break

if __name__ == '__main__':
    main()
