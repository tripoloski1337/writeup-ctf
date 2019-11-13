#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//gcc random_num.c -o random_num -m32 -no-pie -fno-stack-protector -mpreferred-stack-boundary=2 -fno-builtin
void init() {
  setbuf(stdout,0);
}

int main(void) {
  init();
  char nama[100];
  printf("#################################################\n");
  printf("#\tHackFest Random Number Generator\t#\n");
  printf("#################################################\n");
  printf("[+] Please wait, generating random number for you\n");
  sleep(5);
  printf("[+] Random number has been generated!\n");
  printf("[+] Here is your random number : %o\n",&nama);
  printf("[+] What is your name : ");
  fgets(nama,114,stdin);
  printf("[+] Thank you for using our service %s\n",nama);
}
