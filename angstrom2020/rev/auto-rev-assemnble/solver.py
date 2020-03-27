from pwn import *
import subprocess
def main():
    elf = ELF("./autorev_assemble")
    flag = []
    # for i , j in elf.symbols.iteritems():
    for i in range(1000):
        name = i
        # addr = hex(j)
        # if name[:1] == 'f':
        # print name[:1]
        tmp = subprocess.Popen(['gdb' , './autorev_assemble' , '-ex' , 'set disassembly-flavor intel' , '-ex' , 'disas f%s' % i , '-ex' ,"quit"], stdout=PIPE).communicate()[0]
        # print tmp
        pices = tmp.split()[142].replace("al,",'')
        if "0x" not in pices:
            continue
        flag.append(chr(int(pices,16)))
        print "-----------" , i
        print flag
        # input()
    print flag
        # if "flag{" in tmp:
        #     print tmp
        #     break
def maon():
    for i in range(0xff):
        r = remote("shell.actf.co",20203)
        r.sendline(str(i))
        print(r.recv(1))
        r.close()
if __name__ == '__main__':
    main()
