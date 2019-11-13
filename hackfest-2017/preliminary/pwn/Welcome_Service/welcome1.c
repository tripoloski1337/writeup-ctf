/***********************************
input kita “a” masuk ke register EDX dan input “b” masuk ke EAX. Dan terlihat
juga bahwa EIP terhenti ketika menyalin isi register AL ke register EDX. Perlu diketahui bahwa
register AL merupakan register EAX. Mengapa bisa terjadi segmentation fault ? Karena alamat
pada saat EIP ingin menyalin b ke register EDX, isi alamat dari register EDX adalah invalid.
Tepatnya isi register EDX yang seharusnya adalah alamat untuk menyimpan inputan pada gets()
kedua.
Dengan begitu, memungkinkan untuk melakukan GOT Overwrite. Mari kita lihat pada fungsi
main().   Dibawah   fungsi   gets()   kedua   terdapat   fungsi   printf().   Dengan   memanfaatkan   GOT
Overwrite,   kita   bisa   mengganti   fungsi   printf()   menjadi   fungsi   data().
************************************/
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

//gcc welcome1.c -o welcome1 -m32 -no-pie -fno-stack-protector -mpreferred-stack-boundary=2 -fno-builtin

struct hackfest {
  int num;
  char *nama;
};

void init() {
  setbuf(stdout,0);
}

void __data() {
  system("/bin/sh");
  exit(1);
}

void welcome() {
  puts("/***");
  puts("*       __ __         __    ____        __    ____             _ ");
  puts("*      / // /__ _____/ /__ / __/__ ___ / /_  / __/__ _____  __(_)______");
  puts("*     / _  / _ `/ __/  '_// _// -_|_-</ __/ _\\ \\/ -_) __/ |/ / / __/ -_)");
  puts("*    /_//_/\\_,_/\\__/_/\\_\\/_/  \\__/___/\\__/ /___/\\__/_/  |___/_/\\__/\\__/");
  puts("*");
  puts("*/");
  puts("");
}
int main(void) {
  init();
  welcome();

  struct hackfest *h1,*h2,*h3;
  h1 = malloc(sizeof(struct hackfest));
  h1->num = 1;
  h1->nama = malloc(8);

  h2 = malloc(sizeof(struct hackfest));
  h2->num = 2;
  h2->nama = malloc(8);

  h3 = malloc(sizeof(struct hackfest));
  h3->num = 2;
  h3->nama = malloc(8);

  printf("[?] First Name : ");
  gets(h1->nama); // ini akan tersave di ecx
  printf("[?] Mid Name : ");
  gets(h2->nama);
  printf("[?] Last Name : ");
  gets(h3->nama); // ini akan tersave ke eax

  printf("[+] Welcome to HackFest, %s %s! we hope you enjoy our challenge\n",h1->nama,h2->nama); // got overflow
}
