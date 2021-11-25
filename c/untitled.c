#include <stdio.h>

int main() {
    char untitled[5] = {0x73, 0x65, 0x78, 0x0a, 0x00};
    printf("%s", untitled);
    return 0;
}