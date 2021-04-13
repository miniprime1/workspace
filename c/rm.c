#include <stdio.h>

int main(int argc, char* argv[]) {
    if (remove(argv[1]) == 0) { /* pass */ }
    else { printf("rm: Unable to delete the file\n"); }
    return 0;
}