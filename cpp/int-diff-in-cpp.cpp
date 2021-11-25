#include <iostream>
#include <vector>
using namespace std;

struct monomial { 
	double coefficient;
	double exponent; 
};

vector<monomial> derivative(vector<monomial> coefficient) {
	vector<monomial> fx = coefficient;
	vector<monomial> Dfx = {};

	for (int n = 0; n < fx.size(); n++) {
		monomial temp = monomial{ fx[n].coefficient * fx[n].exponent, fx[n].exponent - 1 };
		Dfx.push_back(temp);
	}

	return Dfx;
}

vector<monomial> integrate(vector<monomial> coefficient) {
	vector<monomial> fx = coefficient;
	vector<monomial> Ifx = {};

	for (int n = 0; n < fx.size(); n++) {
		if (fx[n].exponent == -1) { vector<monomial> temp = { monomial{0, 0} }; return temp; }
		monomial temp = monomial{ fx[n].coefficient / (fx[n].exponent + 1), fx[n].exponent + 1 };
		Ifx.push_back(temp);
	}

	return Ifx;
}

int main() {
	// Calculation: f(x)=x^2+3x+2 -> Df(x)=2x+3, If(x)=x^3/3+3x^2/2+2x+C
	vector<monomial> fx = { monomial{1, 2}, monomial{3, 1}, monomial{2, 0}, };
	vector<monomial> Dfx = derivative(fx);
	vector<monomial> Ifx = integrate(fx);

	// Print: Ttile
	cout << "Integrate and Derivative of Polynomial Function in C++" << endl << endl;

	// Print: Result - f(x)
	cout << "f(x)  = ";
	cout << fx[0].coefficient << "x^" << fx[0].exponent;
	for (int n = 1; n < fx.size(); n++) { cout << " + " << fx[n].coefficient << "x^" << fx[n].exponent; }
	cout << endl;

	// Print: Result - Df(x)
	cout << "Df(x) = ";
	cout << Dfx[0].coefficient << "x^" << Dfx[0].exponent;
	for (int n = 1; n < Dfx.size(); n++) { cout << " + " << Dfx[n].coefficient << "x^" << Dfx[n].exponent; }
	cout << endl;

	// Print: Result - If(x)
	cout << "If(x) = ";
	cout << Ifx[0].coefficient << "x^" << Ifx[0].exponent;
	for (int n = 1; n < Ifx.size(); n++) { cout << " + " << Ifx[n].coefficient << "x^" << Ifx[n].exponent; }
	cout << " + " << "const.";
	cout << endl;

	// Function Returning: return 0;
	return 0;
}