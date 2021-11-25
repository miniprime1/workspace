#include <iostream>
#include <string>
#include <iomanip>
#include <complex>
#include <cmath>
#include <cstdlib>
#define PI 3.1415926535897932384626433832795028841971
using namespace std;
using namespace std::complex_literals;


int main() {
    auto solve_constant = [](double a) -> string {
        string result = "";
        if (a == 0) { result = "There is no solution."; }
        else { result = "There is contless solution."; }
        return result;
    };

    int option = 0;
    double a = 0, b = 0, c = 0, d = 0, e = 0;
    double f = 0, g = 0, h = 0, i = 0, j = 0, k = 0;
    double D = 0, L = 0, M = 0, N = 0, P = 0, Q = 0, R = 0, S = 0, T = 0, U = 0;
    complex<double> M_q(0, 0), P_q(0, 0), Q_q(0, 0), R_q(0, 0), S_q(0, 0), T_q(0, 0), U_q(0, 0), V_q(0, 0), W_q(0, 0);
    complex<double> x1(0, 0), x2(0, 0), x3(0, 0), x4(0, 0);
    string result = "null";

    cout << "Equation Solver v1.0" << endl;
    cout << "Copyright (c) 2021 miniprime1" << endl << endl;

    cout << "1. Constant Equation (a=0)" << endl;
    cout << "2. Linear Equation (ax+b=0)" << endl;
    cout << "3. Quadratic Equation (ax^2+bx+c=0)" << endl;
    cout << "4. Cubic Equation (ax^3+bx^2+cx+d=0)" << endl;
    cout << "Enter option: "; cin >> option;

    cout << endl;

    if (option == 1) {
        cout << "Enter a: "; cin >> a;
        result = solve_constant(a);
        cout << endl;
        cout << "Result" << endl;
        cout << result << endl;
    }
    else if (option == 2) {
        cout << "Enter a: "; cin >> a;
        cout << "Enter b: "; cin >> b;
        if (a == 0) { result = solve_constant(b); }
        else { x1 = -b / a; }
        cout << endl;
        cout << "Result" << endl;
        if (result == "null") { 
            if (x1.imag() >= 0) { cout << "x1=" << x1.real() << "+" << x1.imag() << "i" << endl; }
            else { cout << "x1=" << x1.real() << x1.imag() << "i" << endl; }
        }
        else { 
            cout << result << endl; 
        }
    }
    else if (option == 3) {
        cout << "Enter a: "; cin >> a;
        cout << "Enter b: "; cin >> b;
        cout << "Enter c: "; cin >> c;
        if (a == 0) {
            if (b == 0) {
                result = solve_constant(c);
            }
            else {
                x1 = -c / b;
                x2 = nan("");
            }
        }
        else {
            D = pow(b, 2) - 4 * a * c;
            if (D >= 0) {
                D = sqrt(D);
                x1 = (-b + D) / (2 * a);
                x2 = (-b - D) / (2 * a);
            }
            else {
                x1 = nan("");
                x2 = nan("");
            }
        }
        cout << endl;
        cout << "Result" << endl;
        if (result == "null") {
            if (x1.imag() >= 0) { cout << "x1=" << x1.real() << "+" << x1.imag() << "i" << endl; }
            else { cout << "x1=" << x1.real() << x1.imag() << "i" << endl; }
            if (x2.imag() >= 0) { cout << "x2=" << x2.real() << "+" << x2.imag() << "i" << endl; }
            else { cout << "x2=" << x2.real() << x2.imag() << "i" << endl; }
        }
        else {
            cout << result << endl;
        }
    }
    else if (option == 4) {
        cout << "Enter a: "; cin >> a;
        cout << "Enter b: "; cin >> b;
        cout << "Enter c: "; cin >> c;
        cout << "Enter d: "; cin >> d;
        if (a == 0) {
            if (b == 0) {
                if (c == 0) {
                    result = solve_constant(c);
                }
                else {
                    x1 = -d / c;
                    x2 = nan("");
                    x3 = nan("");
                }
            }
            else {
                D = pow(c, 2) - 4 * b * d;
                if (D >= 0) {
                    D = sqrt(D);
                    x1 = (-c + D) / (2 * b);
                    x2 = (-c - D) / (2 * b);
                    x3 = nan("");
                }
                else {
                    x1 = nan("");
                    x2 = nan("");
                    x3 = nan("");
                }
            }
        }
        else {
            f = ((3 * c / a) - (pow(b, 2) / pow(a, 2))) / 3;
            g = (((2 * pow(b, 3)) / pow(a, 3)) - ((9 * b * c) / (pow(a, 2))) + (27 * d / a)) / 27;
            h = (pow(g, 2) / 4) + (pow(f, 3) / 27);

            if (h <= 0) {
                i = sqrt((pow(g, 2) / 4) - h);
                j = cbrt(i);
                k = acos(-(g / (2 * i)));
                L = -j;
                M = cos(k / 3);
                N = sqrt(3) * sin(k / 3);
                P = -(b / (3 * a));
                x1 = 2 * j * M + P;
                x2 = L * (M + N) + P;
                x3 = L * (M - N) + P;
            }
            else {
                R = -(g / 2) + sqrt(h);
                if (R >= 0) { S = cbrt(R); }
                else { S = -cbrt(-R); }
                T = -(g / 2) - sqrt(h);
                if (T >= 0) { U = cbrt(T); }
                else { U = -cbrt(-T); }
                x1 = (S + U) - (b / (3 * a));
                x2 = -(S + U) / 2 - (b / (3 * a)) + (S - U) * sqrt(3) * 0.5i;
                x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * sqrt(3) * 0.5i;
            }
        }
        cout << endl;
        cout << "Result" << endl;
         if (result == "null") {
                if (x1.imag() >= 0) { cout << "x1=" << x1.real() << "+" << x1.imag() << "i" << endl; }
                else { cout << "x1=" << x1.real() << x1.imag() << "i" << endl; }
                if (x2.imag() >= 0) { cout << "x2=" << x2.real() << "+" << x2.imag() << "i" << endl; }
                else { cout << "x2=" << x2.real() << x2.imag() << "i" << endl; }
                if (x3.imag() >= 0) { cout << "x3=" << x3.real() << "+" << x3.imag() << "i" << endl; }
                else { cout << "x3=" << x3.real() << x3.imag() << "i" << endl; }
            }
            else {
                cout << result << endl;
            }
    }

    system("pause"); // for windows users.

    return 0;
}