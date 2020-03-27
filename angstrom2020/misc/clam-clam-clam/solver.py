from pwn import *

def main():
    context.update( log_level="info",)
    r = remote('misc.2020.chall.actf.co',20204)
    print r.recv(100).replace('\r','\')
    # r.interactive()

if __name__ == '__main__':
    main()
