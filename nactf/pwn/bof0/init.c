/* hey you , i know it suspicious but i will 
 * give you a little hint for this challenge.
 * visit this link to see the hint 
 * link : https://www.youtube.com/watch?v=LkCu68gF99Y
 * got it ? :v LOL
 */

/* just a standard input output */
#include <stdio.h>

/* this lib contain signal() */
#include <signal.h>

/* this lib can be used to call exit() */
#include <stdlib.h>

/* 
 * defining size buffer
 */
#define BLOCK_SIZE 10


/* Disable buffering on stdout */
void init(){
	/* THIS IS THE VULNERABILITY ! ! */
	setvbuf(stdout, NULL, _IONBF, 0);
	/* can you realize that ? 
	 * just kidding lol that's not the bug :v
	 */
}

/* this function will print
 * our flag , keep in mind ! !
 */
void win(){
	puts("SIGSEGV triggered!");
	/* defining buffer that can be used
	 * to store our flag to the memory
	 */
	char buf[BLOCK_SIZE];

	/* load the flag */
	FILE* f = fopen("./flag", "r");

	/* if flag not found it will give us
	 * this error message
	 */
	if (f == NULL) 
	{
		/* you should create a counterfeit flag 
		 * file to see if it works or not
		 */
		puts("flag not found , ping me (arsalan) on LINE groups !!! \n");

		/* after print that shit , it will exit 
		 * i mean real exit 
		 */
		exit(-1);
	}
	else
	{
		/* load the flag data to our buffer
		 * remember how much BLOCK_SIZE we have ? 
		 * no idiot ! it's 10 LOL
		 */
		fgets(buf, sizeof(buf), f);

		/* print our buffer 
		 * which is contain our flag
		 */
		printf("flag: %s\n", buf);

		/* end of story */
		exit(0);
	}
}

int main(){
	/* initialize function that we 
	 * make earlier to disable 
	 * buffering on stdout
	 */
	init();

	/* this function will call win function
	 * when Segmentation fault (SIGSEGV)
	 * was triggered , is it the bug ? hmmm
	 * suspicious.
	 */
	signal(SIGSEGV, win); 
	/* can you realize that ? no ? it's oke */

	/* defining our buffer that can be used
	 * to store our input data to memory
	 */
	char bss[BLOCK_SIZE]; // 10 bytes ? yes kinda weird but this is the truth lol
	/* yes i know it's a little bit silly.
	 * sorry for that. but it's must be 10 bytes for now */

	/* print some string and our buffer size
	 */
	printf("buffer[%d] >> ",BLOCK_SIZE);

	/* gets ? hmm have you ever use this function ?
	 * yes ? you have to know that ,this function 
	 * is a little bit dangerous , because it will 
	 * take every single data that you input to memory ,
	 * yes i said 'every' , if we have only 10bytes size of our
	 * buffer in memory and we input more data than
	 * 10bytes what will happen ? , it will overwrite another data on 
	 * memory even (eip/rip) , libc address or anything.
	 * is it a bug ? it's depending to your implementation
	 */
	gets(bss);

	/* good luck ! 
	 */
	return 0;
}