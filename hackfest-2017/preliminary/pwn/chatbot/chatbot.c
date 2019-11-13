#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
//gcc chatbot.c -o chat -m32 -no-pie -fno-stack-protector -mpreferred-stack-boundary=2 -fno-builtin
void init() {
  setbuf(stdout,0);
}

void shell() {
  system("/bin/sh");
  exit(1);
}

int main(void) {
  init();
  char buffer[500];
  printf("#################################################\n");
  printf("#\t\tHackFest Chat Bot\t\t#\n");
  printf("#################################################\n");
  for(int i=0;i<10;i++) {
    printf("\n");
    printf("You : ");
    fgets(buffer,500,stdin);
    buffer[strcspn(buffer, "\n")] = 0;
    printf("Bot : Helloo, have a nice day and good luck, ");
    printf(buffer);
    printf("!\n");
}
}
