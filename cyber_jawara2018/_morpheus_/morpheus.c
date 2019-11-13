/*
 * Cyber Jawara 2018 - Morpheus
 *
 * gcc morpheus.c -o morpheus
 * socat TCP4-LISTEN:41337,reuseaddr,fork EXEC:"./morpheus" > /dev/null 2>&1 &
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char choice;

struct hero {
    char* name;
    int hp;
    int atk;
};

struct hero* a;
struct hero* b;
struct hero* c;

FILE *fp;
char *flag;

void display(int id, struct hero* h) {
    puts("*--------------------*");
    printf("| ID   : %d\n", id);
    printf("| Name : %s\n", h->name);
    printf("| HP   : %u\n", h->hp);
    printf("| ATK  : %u\n", h->atk);
    puts("*--------------------*");
}

void battle() {
    int totalAtk = a->atk + b->atk + c->atk;
    int totalHp = a->hp + b->hp + c->hp;
    if ((totalHp > 2000000000) && (totalAtk > 2000000000)) {
        puts("\n\n ***** You Won! ***** \n\n");

        flag = malloc(128);
        memset(flag, 0, 128);
        fp = fopen("flag.txt", "rb");
        fread(flag, 128, 1, fp);
        fclose(fp);
        puts(flag);

        exit(0);
    } else {
        puts("\n\n ##### You Lose! ##### \n\n");
        exit(0);
    }
}

void changeName() {
    printf("Select ID: ");
    choice = getchar();
    getchar();
    switch (choice) {
        case '1':
            printf("Insert Name: ");
            fgets(a->name, 32, stdin);
            strtok(a->name, "\n");
            break;
        case '2':
            printf("Insert Name: ");
            fgets(b->name, 322, stdin);
            strtok(b->name, "\n");
            break;
        case '3':
            printf("Insert Name: ");
            fgets(c->name, 32, stdin);
            strtok(c->name, "\n");
            break;
    }
}

void trainHP() {
    printf("Select ID: ");
    choice = getchar();
    getchar();
    switch (choice) {
        case '1':
            a->hp++;
            break;
        case '2':
            b->hp++;
            break;
        case '3':
            c->hp++;
            break;
    }
}

void trainATK() {
    printf("Select ID: ");
    choice = getchar();
    getchar();
    switch (choice) {
        case '1':
            a->atk++;
            break;
        case '2':
            b->atk++;
            break;
        case '3':
            c->atk++;
            break;
    }
}

void service() {
    a = (struct hero*)malloc(sizeof(struct hero));
    a->name = malloc(32);
    strcpy(a->name, "Archa");
    a->hp = 100;
    a->atk = 25;

    b = (struct hero*)malloc(sizeof(struct hero));
    b->name = malloc(32);
    strcpy(b->name, "Bhiga");
    b->hp = 110;
    b->atk = 21;

    c = (struct hero*)malloc(sizeof(struct hero));
    c->name = malloc(32);
    strcpy(c->name, "Chrono");
    c->hp = 105;
    c->atk = 22;

    while (1) {
        display(1, a);
        display(2, b);
        display(3, c);
        puts("");
        puts("1) Change Name");
        puts("2) Train HP");
        puts("3) Train ATK");
        puts("4) Battle");
        printf("Choice: ");
        choice = getchar();
        getchar();
        switch (choice) {
            case '1':
                changeName();
                break;
            case '2':
                trainHP();
                break;
            case '3':
                trainATK();
                break;
            case '4':
                battle();
                break;
        }
    }
}

void init() {
    char buff[1];
    buff[0] = 0;
    setvbuf(stdout, buff, _IOFBF, 1);
}

int main() {
    init();
    service();
    return 0;
}
