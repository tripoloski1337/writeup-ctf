#include<stdio.h>
#include <stdlib.h> 

void main(){
	srand(1);
	int v1 = rand();
  	int v2 = rand() + v1;
  	int ini = v2 - rand();

  	printf("%d\n", ini);
}