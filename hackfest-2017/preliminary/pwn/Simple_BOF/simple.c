#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

//gcc simple.c -o simple -m32 -no-pie -fno-stack-protector -mpreferred-stack-boundary=2 -fno-builtin
void init() {
  setbuf(stdout,0);
}

int flag(int key) {
  if(key == 0xd34df146) {
    system("/bin/sh");
  } else {
    printf("[!] Invalid Key : 0x%x\n",key);
  }
  exit(1);
}

int main(void) {
  init();
  int check;
  char nama[40];
  check = 0xcafebabe;
  printf("--- Welcome to HackFest ---\n");
  printf("Nama : ");
  scanf("%s",nama);
  flag(check);
  exit(1);
}
