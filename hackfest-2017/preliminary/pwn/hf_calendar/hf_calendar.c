#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//gcc hf_calendar.c -o hf_calendar -m32 -no-pie -fno-stack-protector -mpreferred-stack-boundary=2 -fno-builtin
void init() {
  setbuf(stdout,0);
}

void run(char* command) {
  system(command);
}

void menu() {
  printf("#########################################################\n");
  printf("#\t\tHackFest Calendar Tools\t\t\t#\n");
  printf("#########################################################\n");
}
int main(void) {
  init();
  char command[16] = "cal -y";
  char name[256];
  menu();
  printf("[+] User ID %o\n",&command);
  printf("[+] Enter your name : ");
  fgets(name,200,stdin);
  name[strcspn(name,"\n")] = 0;
  printf("Have a nice day, ");
  printf(name);
  printf("\n");
  run(command);
}
