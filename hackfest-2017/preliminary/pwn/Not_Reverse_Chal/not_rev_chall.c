#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void init() {
  setbuf(stdout,0);
}

void main() {
  // gcc not_rev_chall.c -o not_rev_chall -m32 -no-pie -fno-stack-protector -mpreferred-stack-boundary=2 -fno-builtin
  init();
  int key[16] = {12, 29, 21, 21, 18, 24, 25, 37, 25, 25, 39, 12, 34, 17, 25, 22};
  int pass_check[16] = {98, 114, 97, 74, 96, 125, 111, 64, 107, 106, 66, 83, 65, 121, 120, 122}; //not_reverse_chal
  char pass_input[32];

  printf("Password : ");
  gets(pass_input);

  if(strlen(pass_input) != 16) {
    puts("Authentication Failed");
    exit(1);
  }

  for(int i=0;i<16;i++) {
    int check = (int)pass_input[i] ^ key[i];
    if(check != pass_check[i]) {
      puts("Authentication Failed");
      exit(1);
    }

  }
  puts("Authentication Success");
}
