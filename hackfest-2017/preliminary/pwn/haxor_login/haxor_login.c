#include <stdio.h>
#include <stdlib.h>

void init() {
  setbuf(stdout,0);
}

int main(void) {
  //gcc haxor_login.c -o haxor_login -m32 -no-pie -fno-stack-protector -fno-builtin -mpreferred-stack-boundary=2 -static
  char username[40];
  char password[48];
  init();
  printf("[?] Username : ");
  gets(username);
  printf("[?] Password for %s : ",username);
  gets(password);
  printf("[!] Authentication Failed\n");
}
