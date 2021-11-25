#include <iostream>
#define PI 3.1415926535897932384626433832795028841971
using namespace std;

namespace math {
	double abs(double x) {
		double result = 0;
		if (x >= 0) result = x;
		else result = -x;
		return result;
	}

	double fact(int x) {
		double result = 1;
		if (x == 0 || x == 1) return 1;
		else for (int i = 1; i < x + 1; i++) { result *= i; }
		return result;
	}

	double pow(double x, int n) {
		if (n == 0) return 1;
		else if ((n % 2) == 0)
			return pow(x * x, n / 2);
		else return x * pow(x * x, (n - 1) / 2);
	}

	double sin(double t) {
		int lim = 84;
		int num = 0;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			num = 2 * n + 1;
			temp = pow(-1, n) * pow(x, num) / fact(num);
			result += temp;
		}
		return result;
	}

	double cos(double t) {
		int lim = 84;
		int num = 0;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			num = 2 * n;
			temp = pow(-1, n) * pow(x, num) / fact(num);
			result += temp;
		}
		return result;
	}

	double exp(double t) {
		int lim = 84;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			temp = pow(x, n) / fact(n);
			result += temp;
		}
		return result;
	}

	double log(double x) {
		double result = 0;
		double temp = 0;
		double limit = (double)1000;

		if (0.0 < x && x < 2.0) {}
		else { return 53303; }

		for (int i = 1; i < limit; i++) {
			temp = pow(x - 1, i) * pow(-1, i + 1) / i;
			result += temp;
		}

		return result;
	}

	double arcsin(double t) {
		int lim = 84;
		int num = 0;

		if (abs(t) <= 1) {}
		else { return 53303; }

		double x = t;
		double result = 0;
		double temp = 0;

		for (int n = 0; n < lim; n++) {
			num = 2 * n + 1;
			temp = (pow(x, num) * fact(2 * n)) / (pow(4, n) * pow(fact(n), 2) * num);
			result += temp;
		}
		return result;
	}

	double arccos(double t) {
		double result = 0;
		if (abs(t) <= 1) {}
		else { return 53303; }
		double x = t;
		result = PI / 2 - arcsin(x);
		return result;
	}

	double arctan(double t) {
		int lim = 84;
		int num = 0;

		if (abs(t) <= 1) {}
		else { return 53303; }

		double x = t;
		double result = 0;
		double temp = 0;

		for (int n = 0; n < lim; n++) {
			num = 2 * n + 1;
			temp = (pow(x, num) * pow(-1, n)) / num;
			result += temp;
		}
		return result;
	}

	double sinh(double t) {
		int lim = 84;
		int num = 0;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			num = 2 * n + 1;
			temp = pow(x, num) / fact(num);
			result += temp;
		}
		return result;
	}

	double cosh(double t) {
		int lim = 84;
		int num = 0;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			num = 2 * n;
			temp = pow(x, num) / fact(num);
			result += temp;
		}
		return result;
	}

	double arsinh(double t) {
		int lim = 84;
		int num = 0;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			num = 2 * n + 1;
			temp = (pow(-1, n) * pow(x, num) * fact(2 * n)) / (pow(4, n) * pow(fact(n), 2) * num);
			result += temp;
		}
		return result;
	}

	double artanh(double t) {
		int lim = 84;
		int num = 0;
		double x = t;
		double result = 0;
		double temp = 0;
		for (int n = 0; n < lim; n++) {
			num = 2 * n + 1;
			temp = pow(x, num) / num;
			result += temp;
		}
		return result;
	}
}

int main() {
	int option = 0;
	double x = 0, y = 0;
	bool outofrange_error = false;

	cout << "Taylor Series Calculator v1.0" << endl;
	cout << "Copyright (c) 20201 miniprime1." << endl << endl;

	cout << "Options" << endl;
	cout << "1. Sine (sin(x), for all x)" << endl;
	cout << "2. Cosine (sin(x), for all x)" << endl;
	cout << "3. Exponential (exp(x), for all x)" << endl;
	cout << "4. Natural log (log(x), for 0<x<2)" << endl;
	cout << "5. Arc Sine (arcsin(x), for abs(x)<=1)" << endl;
	cout << "6. Arc Cosine (arccos(x), for abs(x)<=1)" << endl;
	cout << "7. Arc Tangent (arccos(x), for abs(x)<=1)" << endl;
	cout << "8. Hyperbolic Sine (sinh(x), for all x)" << endl;
	cout << "9. Hyperbolic Cosine (cosh(x), for all x)" << endl;
	cout << "10. Hyperbolic Arc Sine (arcsin(x), for abs(x)<=1)" << endl;
	cout << "11. Hyperbolic Arc Tangent (arctan(x), for abs(x)<1)" << endl;
	cout << "Enter choice: ";
	cin >> option;

	cout << endl;

	if (option == 1) {
		cout << "Enter x: ";
		cin >> x;
		y = math::sin(x);
		cout << endl << "Result" << endl;
		cout << "sin" << "(" << x << ")" << " = " << y << endl;
	}
	else if (option == 2) {
		cout << "Enter x: ";
		cin >> x;
		y = math::cos(x);
		cout << endl << "Result" << endl;
		cout << "cos" << "(" << x << ")" << " = " << y << endl;
	}
	else if (option == 3) {
		cout << "Enter x: ";
		cin >> x;
		y = math::exp(x);
		cout << endl << "Result" << endl;
		cout << "exp" << "(" << x << ")" << " = " << y << endl;
	}
	else if (option == 4) {
		cout << "Enter x: ";
		cin >> x;
		if (0 < x && x < 2) y = math::log(x);
		else outofrange_error = true; 
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
			return 1;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "log" << "(" << x << ")" << " = " << y << endl;
		}
	}
	else if (option == 5) {
		cout << "Enter x: ";
		cin >> x;
		if (abs(x) <= 1) y = math::arcsin(x);
		else outofrange_error = true;
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
			return 1;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "arcsin" << "(" << x << ")" << " = " << y << endl;
		}
	}
	else if (option == 6) {
		cout << "Enter x: ";
		cin >> x;
		if (abs(x) <= 1) y = math::arccos(x);
		else outofrange_error = true;
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
			return 1;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "arccos" << "(" << x << ")" << " = " << y << endl;
		}
	}
	else if (option == 7) {
		cout << "Enter x: ";
		cin >> x;
		if (abs(x) <= 1) y = math::arctan(x);
		else outofrange_error = true;
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
			return 1;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "arctan" << "(" << x << ")" << " = " << y << endl;
		}
	}
	else if (option == 8) {
		cout << "Enter x: ";
		cin >> x;
		y = math::sinh(x);
		cout << endl << "Result" << endl;
		cout << "sinh" << "(" << x << ")" << " = " << y << endl;
	}
	else if (option == 9) {
		cout << "Enter x: ";
		cin >> x;
		y = math::cosh(x);
		cout << endl << "Result" << endl;
		cout << "cosh" << "(" << x << ")" << " = " << y << endl;
	}
	else if (option == 10) {
		cout << "Enter x: ";
		cin >> x;
		if (abs(x) <= 1) y = math::arsinh(x);
		else outofrange_error = true;
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
			return 1;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "arsinh" << "(" << x << ")" << " = " << y << endl;
		}
	}
	else if (option == 11) {
		cout << "Enter x: ";
		cin >> x;
		if (abs(x) < 1) y = math::artanh(x);
		else outofrange_error = true;
		if (outofrange_error) {
			cout << endl << "Error: an error occurred; Out of range error" << endl;
			return 1;
		}
		else {
			cout << endl << "Result" << endl;
			cout << "artanh" << "(" << x << ")" << " = " << y << endl;
		}
	}

	return 0;
}