#include <cstdio>
#include <cmath>

double derive(double (*f)(double), double a)
{
    const double h = 1.0e-6;
    double x1 = a - h;
    double x2 = a + h;
    double y1 = f(x1);
    double y2 = f(x2);
    return (y2 - y1) / (x2 - x1);
}

int main() {
    // Variables
    int opt;
    double a;
    
    // About & Copyright
    printf("Derivative Calculator v1.0\n");
    printf("Copyright (c) 2021 miniprime1.\n");
    printf("[Math: f'(a)]\n");
    
    // Option
    printf("\nOptions\n");
    printf("1. Derivative of Trigonometric functions\n");
    printf("2. Derivative of Exponential and logarithmic functions\n");
    printf("3. Derivative of Power functions\n");
    printf("Enter options: "); scanf("%d", &opt);
    printf("\n");
    
    // Main
    if (opt == 1) {
        printf("Detailed options\n");
        printf("1. Compute derivative of cosine\n");
        printf("2. Compute derivative of sine\n");
        printf("3. Compute derivative of tangent\n");
        printf("4. Compute derivative of arc cosine\n");
        printf("5. Compute derivative of arc sine\n");
        printf("6. Compute derivative of arc tangent\n");
        printf("Enter choice: ");
        scanf("%d", &opt);
        printf("\n");
        
		if (opt == 1) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(cos, a);
			printf("\ncos'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 2) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(sin, a);
			printf("\nsin'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 3) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(tan, a);
			printf("\ntan'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 4) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(acos, a);
			printf("\narccos'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 5) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(asin, a);
			printf("\narcsin'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 6) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(atan, a);
			printf("\narctan'(%lf) = %lf\n", a, der);
			return 0;
		} else {
			printf("Error: invalid choice\n");
			return 1;
		}
	} else if (opt == 2) {
	    printf("Detailed options\n");
		printf("1. Compute derivative of exponential function\n");
		printf("2. Compute derivative of natural logarithm\n");
		printf("3. Compute derivative of common logarithm\n");
		printf("Enter choice: ");
		scanf("%d", &opt);
        printf("\n");
        
	    if (opt == 1) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(exp, a);
			printf("\nexp'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 2) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(log, a);
			printf("\nlog'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 3) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(log10, a);
			printf("\nlog10'(%lf) = %lf\n", a, der);
			return 0;
		} else {
			printf("Error: invalid choice\n");
			return 1;
		}
	} else if (opt == 3) {
	    printf("Detailed options\n");
		printf("1. Compute derivative of square root\n");
		printf("2. Compute derivative of cubic root\n");
		printf("Enter choice: ");
		scanf("%d", &opt);
        printf("\n");
        
	    if (opt == 1) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(sqrt, a);
			printf("\nsqrt'(%lf) = %lf\n", a, der);
			return 0;
		} else if (opt == 2) {
			printf("Enter a: ");
			scanf("%lf", &a);
			double der = derive(cbrt, a);
			printf("\ncbrt'(%lf) = %lf\n", a, der);
			return 0;
		} else {
			printf("Error: invalid choice\n");
			return 1;
		}
	} else {
		printf("Error: invalid choice\n");
		return 1;
	}
	
    return 0;
}