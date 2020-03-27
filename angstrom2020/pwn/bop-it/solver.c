#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>

int main(){
  srand(time(NULL));

  const char *actions[] = {"Bop it!\n", "Twist it!\n", "Pull it!\n", "Flag it!\n"};

  char c;
	char *action = actions[rand()%4];
  write(1, action, 1);
  // wrong[strlen(wrong)-3] = action[0];
  // write(1, wrong, strlen(wrong));
}
