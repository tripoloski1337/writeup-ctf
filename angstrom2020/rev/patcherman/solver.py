def smh(d , i):
    return d + i

def shift1(a , b):
    return (a << b) & 1

def dosmh(keymaybe):
    v0 = shift1(keymaybe, 0)
    v1 = shift1(keymaybe, 2) ^ v0
    v2 = shift1(keymaybe, 3) ^ v1
    v3 = shift1(keymaybe, 5)
    keymaybe = keymaybe >> 1
    keymaybe |= (v2 ^ v3) << 31
    return keymaybe

def main():
    enc = [  0xEA, 0x83, 0xD8, 0x5C, 0xC0, 0x80, 0x66, 0xEF, 0x86, 0x70,
    0xCC, 0xAF, 0x7F, 0xB8, 0x3A, 0x7E, 0x3A, 0x77, 0xC5, 0x7D,
    0x35, 0x80, 0x20, 0x38, 0xF5, 0xC3, 0x56, 0x04, 0xFF, 0xFF,
    0xFF, 0xFF]
    key1 = 0x0F00DBABE
    x = dosmh(key1)
    for x in range(0xff):
        flag = ['' for i in range(len(enc))]
        for i in range(len(enc)):
            flag[i] = chr((smh((enc[i] ^ 0x1337beef ), dosmh(x))) % 0xff)
        # if "a" in flag:
        k = ''
        for i in flag:
            k += i
        print k

if __name__ == '__main__':
    main()
