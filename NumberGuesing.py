import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it correctly.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue

        if guess < 1 or guess > 100:
            print("Out of range! Please enter a number between 1 and 100.\n")
            continue 

        attempts += 1

        if guess < number_to_guess:
            print("Too low!\n")
        elif guess > number_to_guess:
            print("Too high!\n")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")

number_guessing_game()
