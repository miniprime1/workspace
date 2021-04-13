#include <sys/stat.h> 
#include <sys/types.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    int check;
    check = mkdir(argv[1], 0700);
    if (!check) { /* pass */ }
    else { printf("Error: unable to create directory"); return 1; }
    return 0;
}