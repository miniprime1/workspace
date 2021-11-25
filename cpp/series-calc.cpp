#include <iostream>
using namespace std;

double pow(double x, int n) {
	if (n == 0) return 1;
	else if ((n % 2) == 0)
		return pow(x * x, n / 2);
	else return x * pow(x * x, (n - 1) / 2);
}

int main() {
	int option = 0;
	double a = 0, r = 0, d = 0, n = 0;
	double sum = 0;
	string message = "";

	cout << "Series Calculator v1.0" << endl;
	cout << "Copyright (c) 2021 miniprime1." << endl << endl;

	cout << "Options" << endl;
	cout << "1. Arithmetic series (a(n) = a + (n-1)d)" << endl;
	cout << "2. Definite Geometric series (a(n) = a*r^(n-1))" << endl;
	cout << "3. Infinite Geometric series  (a(n) = a*r^(n-1))" << endl;
	cout << "Enter choice: ";
	cin >> option;

	cout << endl;

	if (option == 1) {
		cout << "Enter the first term of the sequence: ";
		cin >> a;
		cout << "Enter the common difference between terms: ";
		cin >> d;
		cout << "Enter limit of series: ";
		cin >> n;
		sum = (2 * a + (n - 1) * d) * n / 2;
		cout << endl << "Result" << endl;
		cout << "Sum(" << a << "+" << d << "(k-1), (k=1, " << n << "))" << " = " << sum << endl;
	}
	else if (option == 2) {
		cout << "Enter the first term of the sequence: ";
		cin >> a;
		cout << "Enter the common ratio between terms: ";
		cin >> r;
		cout << "Enter limit of series: ";
		cin >> n;
		if (r == 1) {
			sum = n * a;
		}
		else {
			sum = (a * (1 - pow(r, n))) / (1 - r);
		}
		cout << endl << "Result" << endl;
		cout << "Sum(" << a << "*" << r << "^(k-1), (k=1, " << n << "))" << " = " << sum << endl;
	}
	else if (option == 3) {
		cout << "Enter the first term of the sequence: ";
		cin >> a;
		cout << "Enter the common ratio between terms: ";
		cin >> r;
		if (r == 1) sum = n * a;
		else if (r < 1) sum = a / (1 - r);
		else if (r == -1) message = "diverge";
		else message = "diverge";
		if (message == "") {
			cout << endl << "Result" << endl;
			cout << "Sum(" << a << "*" << r << "^(k-1), (k=1, infinity))" << " = " << sum << endl;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "Sum(" << a << "*" << r << "^(k-1), (k=1, infinity))" << " = " << "(" << message << ")" << endl;
		}
	}
	else {
		cout << "Error: invalid choice" << endl;
		return 1;
	}

	return 0;
}