#JC 2nd Fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")

        #Could not correct the answer
        guess = int(guess)

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        #It was an elif it would not run if this was not fixed
        else:
            print("Too low! Try again.")  
        #Was not increasing the attempt tracker so first psrt useless
        attempts += 1

        continue
    print("Game Over. Thanks for playing!")
start_game()