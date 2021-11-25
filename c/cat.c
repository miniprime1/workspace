#include <stdio.h>

int main(int argc, char* argv[]) {
    char str[2048];
    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL) { printf("cat: %s: No such file or directory\n", argv[1]); return 1; }
    while (fgets(str, 2048, fp) != NULL) { printf("%s", str); }
    fclose(fp);
    return 0;
}