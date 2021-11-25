#include <iostream>
using namespace std;

double factorial(int x) {
	double result = 1;
	if (x == 0 || x == 1) return 1;
	else for (int i = 1; i < x+1; i++) { result *= i; }
	return result;
}

double power(double x, int n) {
	if (n == 0) return 1;
	else if ((n % 2) == 0)
		return power(x * x, n / 2);
	else return x * power(x * x, (n - 1) / 2);
}

double exponential(double t) {
	int lim = 84;
	double x = t;
	double result = 0;
	double temp = 0;
	for (int n = 0; n < lim; n++) {
		temp = power(x, n) / factorial(n);
		result += temp;
	}
	return result;
}

int main() {
	double x;
	double y;

	cout << "Exponential Calculator v1.0" << endl;
	cout << "Copyright (c) 2021 miniprime1." << endl << endl;

	cout << "Enter input: ";
	cin >> x;

	y = exponential(x);

	cout << endl << "Result" << endl;
	cout << "exp" << "(" << x << ")" << " = " << y << endl;

	return 0;
}