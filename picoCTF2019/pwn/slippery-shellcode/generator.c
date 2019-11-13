#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int get_off(){
	int offset = (rand() % 256) + 1;
	return offset;
}

int main(){
	printf("%d\n", get_off());
	return 0;
}
