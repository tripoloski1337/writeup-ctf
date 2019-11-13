#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//gcc lower_check.c -o lower_check -m64 -no-pie -fno-stack-protector
void init() {
  setbuf(stdout,0);
}

void main() {
  char check[128];
  init();
  puts("--- String Lowercase Checker ---");
  printf("[+] String to check : ");
  gets(check);
  for(int i=0;i<strlen(check);i++) {
    if((int)check[i] >= 97 && (int)check[i] <=122) {
      continue;
    } else {
      puts("[+] The Result : False");
      exit(1);
    }
  }
  puts("[+] The Result : True");
}
