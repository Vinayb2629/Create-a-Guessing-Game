import random

def guessing_game():
    print("Welcome to the Enhanced Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    while True:
        try:
            difficulty = int(input("Select a difficulty (1, 2, or 3): "))
            if difficulty == 1:
                range_max = 50
                break
            elif difficulty == 2:
                range_max = 100
                break
            elif difficulty == 3:
                range_max = 200
                break
            else:
                print("Please choose a valid difficulty level.")
        except ValueError:
            print("Please enter a number.")

    number_to_guess = random.randint(1, range_max)
    attempts = 0
    print(f"Guess the number I'm thinking of between 1 and {range_max}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low, try again.")
                if attempts % 4 == 0:  # Gives a hint every 4 attempts
                    hint = random.choice(['higher', 'lower'])
                    print(f"Hint: Try a bit {hint}.")
            elif guess > number_to_guess:
                print("Too high, try again.")
                if attempts % 4 == 0:  # Gives a hint every 4 attempts
                    hint = random.choice(['higher', 'lower'])
                    print(f"Hint: Try a bit {hint}.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                if attempts < 5:
                    print("Wow! You're a natural at this!")
                elif attempts < 10:
                    print("Nicely done, you've got a good intuition for this game!")
                else:
                    print("You got it! It took some tries, but you made it!")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
