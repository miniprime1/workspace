#include <stdio.h>
#include <math.h>

int main() {
    double G = 6.6743015 * pow(10, -11);
    double K = pow(10, 3);
    double R = 6.371 * K;
    double M = 5.972 * pow(10, 24);
    double F = G * M / pow(R*K, 2);
    printf("%1.48f\n", F);
    return 0;
}