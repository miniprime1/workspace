#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <unistd.h>

int main() {
    char* cwd = (char*)malloc(sizeof(char) * 1024);
    DIR* dir = NULL;
    struct dirent* entry = NULL;
    getcwd(cwd, 1024);

    if((dir = opendir(cwd)) == NULL) {
        printf("ls: No such file or directory");
        exit(1);
    }

    while((entry = readdir(dir)) != NULL) {
        printf("%s\n", entry->d_name);
    }

    free(cwd);
    closedir(dir);

    return 0;
}