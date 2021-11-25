#include <unistd.h>
#include <stdio.h>
#include <limits.h>

int main() {
   char pwd[8192];
   if (getcwd(pwd, sizeof(pwd)) != NULL) {
       printf("%s\n", pwd);
   } else {
       printf("Error!\n");
       return 1;
   }
   return 0;
}