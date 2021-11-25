/* *****************************************
   Edit, version 1.0
   Copyright (c) 2020 miniprime1

   Description: Simple CLI Text Editor
   License: MIT License (miniprime1, 2021)
   Language: C
   Compiler: GCC, Clang, VC++, Xcode
   ***************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char data[4096];
    char path[4096];
    int choice;

    printf("Edit, version 1.0\n");
    printf("Copyright (c) 2020 miniprime1\n");
    printf("\nOptions");
    printf("\n1. Write Mode (w)");
    printf("\n2. Read Mode (r)");
    printf("\n3. Append Mode (a)");
    printf("\n4. Exit (x)");
    printf("\nEnter choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("\nEnter path of file to save: ");
        scanf("%s", path);
        FILE* fp = fopen(path, "wt");
        if (fp == NULL) { printf("\n\nError: failed to create the file\n"); printf("\nPress enter key to exit"); getchar(); return 1; }
        printf("\n");
        printf("\n[ Enter text to write (To exit, type \"EXIT\"): ]");
        printf("\n==================================================\n");
        while (1) {
            fgets(data, 4096, stdin);
            if (strcmp(data, "EXIT\n") == 0) { break; }
            fputs(data, fp);
            fseek(fp, 0, SEEK_SET);
        }
        printf("==================================================\n");
        fclose(fp);
    } else if (choice == 2) {
        printf("\nEnter path of file to open: ");
        scanf("%s", path);
        FILE* fp = fopen(path, "rt");
        if (fp == NULL) { printf("\n\nError: failed to open the file\n"); printf("\nPress enter key to exit"); getchar(); return 1; }
        printf("\n");
        printf("\n==================================================\n");
        while (fgets(data, 4096, fp) != NULL) { printf("%s\n", data); }
        printf("==================================================\n");
        fclose(fp);
    } else if (choice == 3) {
        printf("\nEnter path of file to open/save: ");
        scanf("%s", path);
        FILE* fp = fopen(path, "at");
        if (fp == NULL) { printf("\n\nError: failed to open the file\n"); printf("\nPress enter key to exit"); getchar(); return 1; }
        printf("\n");
        printf("\n[ Enter text to append (To exit, type \"EXIT\"): ]");
        printf("\n==================================================\n");
        while (1) {
            fgets(data, 4096, stdin);
            if (strcmp(data, "EXIT\n") == 0) { break; }
            fputs(data, fp);
            fseek(fp, 0, SEEK_SET);
        }
        printf("==================================================\n");
        fclose(fp);
    } else if (choice == 4) {
        return 0;
    } else {
        printf("\nError: invalid choice!");
        return 1;
    }

    return 0;
}
