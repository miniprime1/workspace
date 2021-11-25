#include <stdio.h>
#include <time.h>

int main() {
    time_t t;
    time(&t);
    char* dt = ctime(&t);
    printf("%s", dt);
    return 0;
}