#include <iostream>
using namespace std;

int main() {
    double num1, num2;   // variables to store numbers
    char operation;      // variable to store operator (+, -, *, /)

    // Asking user for input
    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    cout << "Choose operation (+, -, *, /): ";
    cin >> operation;

    // Performing operations based on user choice
    switch (operation) {
        case '+':
            cout << "Result: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Result: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Result: " << num1 * num2 << endl;
            break;
        case '/':
            if (num2 != 0)
                cout << "Result: " << num1 / num2 << endl;
            else
                cout << "Error: Division by zero is not allowed!" << endl;
            break;
        default:
            cout << "Invalid operation!" << endl;
    }

    return 0;
}
