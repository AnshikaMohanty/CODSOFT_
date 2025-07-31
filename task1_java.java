import java.util.Scanner;
import java.util.Random;

public class NumberGuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int maxAttempts = 5;
        int score = 0;
        boolean playAgain = true;

        System.out.println("🎮 Welcome to the Number Guessing Game!");

        while (playAgain) {
            int numberToGuess = random.nextInt(100) + 1;  // Random number from 1 to 100
            int attemptsLeft = maxAttempts;
            boolean guessedCorrectly = false;

            System.out.println("\n🔢 I have selected a number between 1 and 100.");
            System.out.println("💡 You have " + maxAttempts + " attempts to guess it!");

            while (attemptsLeft > 0) {
                System.out.print("Enter your guess: ");
                int userGuess = scanner.nextInt();

                if (userGuess == numberToGuess) {
                    System.out.println("✅ Congratulations! You guessed the correct number!");
                    guessedCorrectly = true;
                    score++;
                    break;
                } else if (userGuess > numberToGuess) {
                    System.out.println("📉 Too high! Try again.");
                } else {
                    System.out.println("📈 Too low! Try again.");
                }

                attemptsLeft--;
                System.out.println("🔁 Attempts remaining: " + attemptsLeft);
            }

            if (!guessedCorrectly) {
                System.out.println("❌ You've run out of attempts. The number was: " + numberToGuess);
            }

            System.out.print("\n🎲 Do you want to play another round? (yes/no): ");
            String response = scanner.next();

            if (!response.equalsIgnoreCase("yes")) {
                playAgain = false;
            }
        }

        System.out.println("\n🏁 Game over! Your final score: " + score);
        scanner.close();
    }
}
