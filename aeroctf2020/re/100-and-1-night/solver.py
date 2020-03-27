from pwn import *

def token():
    # file : 4e0cb6fb5fb446d1c92ede2ed8780188
    raw = '671B6B6B6C2068221C1D196B1D1E1E6B6C1B1B1D1822221B6D1E671E686B6E22'
    # ((a1[i] + 5) ^ 0x13) - 13;
    p = ''
    for i in raw.decode('hex'):
        p += chr(((ord(i) + 13) ^ 0x13) - 5)
    return p

def main():
    tok = token()
    while True:
        r = remote("tasks.aeroctf.com",44324)
        r.recvuntil("Enter valid token to binary with name ")
        x = r.recv(34)
        x = x.replace("<",'').replace('>','')
        # if x == '4e0cb6fb5fb446d1c92ede2ed8780188':
            # r.sendline(tok)
        r.sendlineafter("Token:",("x"*32))
        # r.interactive()
        print r.recvline()
        r.close()
        # break

if __name__ == '__main__':
    main()
