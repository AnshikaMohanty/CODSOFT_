#include <iostream>
#include <cstdlib>   // for rand() and srand()
#include <ctime>     // for time()

using namespace std;

int main() {
    // Seed the random number generator with current time
    srand(time(0));

    int secretNumber = rand() % 100 + 1; // Random number between 1 and 100
    int guess;

    cout << "Guess the number (between 1 and 100): ";

    // Loop until user guesses correctly
    do {
        cin >> guess;

        if (guess > secretNumber) {
            cout << "Too high! Try again: ";
        } else if (guess < secretNumber) {
            cout << "Too low! Try again: ";
        } else {
            cout << "🎉 Correct! You guessed the number." << endl;
        }

    } while (guess != secretNumber);

    return 0;
}
