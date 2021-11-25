#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int com = rand() % 3;
    int user;

    while (com == 0) {
        com = rand() % 3;
    }

    printf("Rock Paper Scissors v1.0\n");
    printf("Copyright (c) 2020 miniprime1\n");

    printf("\nYour turn!\n");
    printf("Enter input (1:Rock; 2:Paper; 3:Scissors): ");
    scanf("%d", &user);

    printf("\nComputer turn!\n");
    printf("Enter input (1:Rock; 2:Paper; 3:Scissors): %d", com);

    printf("\n");

    if (user == 1) {
        printf("\nYour choice: Rock");
    } else if (user == 2) {
        printf("\nYour choice: Paper");
    } else if (user == 3) {
        printf("\nYour choice: Scissors");
    } else {
        printf("\n\nError: invalid choice");
        exit(0);
    }

    if (com == 1) {
        printf("\nComputer choice: Rock");
    } else if (com == 2) {
        printf("\nComputer choice: Paper");
    } else if (com == 3) {
        printf("\nComputer choice: Scissors");
    } else {
        printf("\nError: C++ Runtime Error");
        exit(0);
    }

    printf("\n\n");

    if (com == user) {
        printf("It's draw!\n");
    } else if (user == 3 && com == 2) {
        printf("You win!\n");
    } else if (user == 2 && com == 1) {
        printf("You win!\n");
    } else if (user == 1 && com == 3) {
        printf("You win!\n");
    } else {
        printf("Computer win!\n");
    }
    
    return 0;
}
