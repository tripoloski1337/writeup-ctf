#include <stdio.h>
#include <string.h>

void init() {
  setbuf(stdout,0);
}
//gcc string_to_hex.c -o string_to_hex -m64 -no-pie -fno-stack-protector -static
int main(void) {
  init();
  char convert[256];
  printf("[?] Give me String : ");
  gets(convert);
  for(int i=0;i<strlen(convert);i++) {
    printf("%x",convert[i]);
  }
  printf("\n");
}
