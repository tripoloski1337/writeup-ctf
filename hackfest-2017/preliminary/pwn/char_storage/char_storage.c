#include <stdio.h>
#include <stdlib.h>

//gcc char_storage.c -o char_storage -fstack-protector -m32 -no-pie -fno-builtin -mpreferred-stack-boundary=2 -static
void init() {
  setbuf(stdout,0);
}

void menu() {
  printf("#########################################################\n");
  printf("#\t\tHackFest Character Storage\t\t#\n");
  printf("#########################################################\n");
  puts("#\t1. Insert char into the stack\t\t\t#");
  puts("#\t2. View inserted char from the stack\t\t#");
  puts("#\t3. Exit\t\t\t\t\t\t#");
  printf("#########################################################\n");
  printf("Your Choice : ");
}

int main(void) {
  init();
  char storage[500];
  char newline;
  int pilihan = 0;
  int index_pil;
  int index_inc = 0;

  while(pilihan != 3 && pilihan >=0 && pilihan < 3) {
    menu();
    scanf("%d",&pilihan);

    switch(pilihan) {
      case 1:
      printf("Insert character : ");
      scanf("%c",&newline);
      scanf("%c",&storage[index_inc]);
      printf("The stack at index %d has been written\n",index_inc);
      index_inc++;

      break;

      case 2:
      printf("Choose character index : ");
      scanf("%d",&index_pil);
      printf("The character at index %d is %d in ASCII\n",index_pil,storage[index_pil]);
      break;

      case 3:
      printf("Thank you for using our service\n");
      break;

      default:
      printf("Invalid choice\n");
      exit(1);
      break;


    }

  }
}
