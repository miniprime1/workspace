/* *****************************************
   Edit, version 1.0
   Copyright (c) 2020 miniprime1

   Description: Simple CLI Text Editor
   License: MIT License (miniprime1, 2021)
   Language: C++
   Compiler: VC++, Clang, G++
   ***************************************** */

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

int main() {
	string data;
    string path;
	int choice;

	cout << "Edit, version 1.0\n";
	cout << "Copyright (c) 2020 miniprime1\n";
	cout << "\nOptions";
	cout << "\n1. Write Mode (w)";
	cout << "\n2. Read Mode (r)";
	cout << "\n3. Append Mode (a)";
	cout << "\n4. Exit (x)";
	cout << "\nEnter choice: ";
	scanf("%d", &choice);

	if (choice == 1) {
		cout << "\nEnter path of file to save: ";
		cin >> path;
        ofstream fp(path, ios_base::out);
        if (fp.is_open()) {
            cout << "\n";
		    cout << "\n[ Enter text to write (To exit, type \"EXIT\"): ]";
		    cout << "\n==================================================\n";
		    while (1) {
			    getline(cin, data);
			    if (data == "EXIT") { break; }
			    fp << data << '\n';
                fp.seekp(0, ios::beg);
		    }
		    cout << "==================================================\n";
		    fp.close();
        } else {
            cout << "\n\nError: failed to create the file\n"; 
            cout << "\nPress enter key to exit"; 
            getchar(); return 1;
        }
	} else if (choice == 2) {
		cout << "\nEnter path of file to open: ";
		cin >> path;
		ifstream fp(path, ios_base::in);
        if (fp.is_open()) {
            cout << "\n";
		    cout << "\n==================================================\n";
		    while (getline(fp, data)) { cout << data << "\n"; }
		    cout << "==================================================\n";
		    fp.close();
        } else {
            cout << "\n\nError: failed to create the file\n"; 
            cout << "\nPress enter key to exit"; 
            getchar(); return 1;
        }
	} else if (choice == 3) {
		cout << "\nEnter path of file to open/save: ";
		cin >> path;
        ofstream fp(path, ios_base::app); 
        if (fp.is_open()) {
            cout << "\n";
		    cout << "\n[ Enter text to append (To exit, type \"EXIT\"): ]";
		    cout << "\n==================================================\n";
		    while (1) {
			    getline(cin, data);
			    if (data == "EXIT") { break; }
			    fp << data << '\n';
                fp.seekp(0, ios::beg);
		    }
		    cout << "==================================================\n";
		    fp.close();
        } else {
            cout << "\n\nError: failed to create the file\n"; 
            cout << "\nPress enter key to exit"; 
            getchar(); return 1;
        }
	} else if (choice == 4) {
		return 0;
	} else {
		cout << "\nError: invalid choice!";
		return 1;
	}

	return 0;
}