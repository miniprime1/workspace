#include <stdio.h>

int main() {
    char sex[5] = {0x73, 0x65, 0x78, 0x0a, 0x00};
    printf("%s", sex);
    return 0;
}