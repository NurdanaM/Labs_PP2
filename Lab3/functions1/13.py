import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    num_to_guess = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            attempts += 1

            if guess < num_to_guess:
                print("Your guess is too low.")
            elif guess > num_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Enter a valid number!")

guess_the_number()