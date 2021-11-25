#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

long double ln(long double x) {
	long double result = 0;
	long double temp = 0;
	long double limit = (double)1000;

	if (0.0 < x && x < 2.0) {}
	else {return 504;}

	for (int i = 1; i < limit; i++) {
		temp = pow(x-1, i) * pow(-1, i+1) / i;
		result += temp;
	}

	return result;
}

int main() {
	long double x = 1;
	long double result = 0;

	bool outofrange_error = false;

	cout << "Natural logarithm calculator v1.0" << endl;
	cout << "Copyright (c) 2021 miniprime1" << endl << endl;

	cout << "Enter input (0<x<2): ";
	cin >> x;

	if (0.0 < x && x < 2.0) { bool outofrange_error = false; }
	else { bool outofrange_error = true; }

	result = ln(x);

	if (result == 504) { 
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
		}
		else {
			cout << endl << "Error: an error occurred; Unknown error" << endl;
		}
	}
	else { 
		cout << endl << "Result" << endl;
		cout << "ln" << "(" << x << ")" << " = " << result << endl; 
	}

	return 0;
}