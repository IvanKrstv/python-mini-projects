import os
from random import randint
from time import sleep
import levels

# Function for checking if the input is a correct value and in range
def check_input(variable):
    try:
        variable
    except ValueError:
        print("Invalid input! Please enter a number.")
        return False
    if variable not in range(a, b + 1):
        print(f"The number is not in the given range. Please enter a number in the range between {a} and {b}")
        return False
    return True
def clear_screen():
    # Check if the OS is Windows
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux or macOS

count_of_games = 0 # Keeping track of the number of games for the levels

# Welcome messages
print('Welcome to the game "GuessTheNumber"\n')

close_program = False # Variable for exiting the loop
while not close_program:

    level = levels.user_level() # Define the level

    # Limits of the range
    a = 1
    b = levels.limit_range()

    print(f"Your opponent has thought of a number in the range between {a} and {b}. Can you guess it correctly? Let's see.")

    computer_number = randint(a, b) # Randomly generated number in the given range
    attempts = 0

    # Getting user's choice
    choice = int(input("Enter your guess: "))
    while not check_input(choice):
        choice = int(input("Enter your guess: "))

    # Playing the game while the user's number is not correct
    while choice != computer_number:
        attempts += 1
        if choice > computer_number:
            print("Oops...too high. The number is lower.")
        else:
            print("Oops...too low. The number is higher.")
        choice = int(input("Enter your guess: "))
        while not check_input(choice):
            choice = int(input("Enter your guess: "))

    # The final message after the user guesses the number
    final_message = f"\nBINGO! You got it after {attempts}. Congratulations!"
    if attempts > 7:
        final_message += " But there is still room for improvement."
    else:
        final_message += " This is a really good result, it seems you have a great intuition."
    print(final_message)
    count_of_games += 1

    # Asking if the player wants to play again
    play_again = input("\nWould you like to play again? Type Yes or No: ").lower()
    while True:
        if play_again in ["yes", "yea", "ye", "sure", "y"]:
            print("Great!😃 Let's do it. ")
            sleep(3)
            clear_screen()
            break
        elif play_again in ["no", "n", "nah", "ne"]:
            print("Goodbye! Have a nice day")
            sleep(3)
            close_program = True
        else:
            play_again = input("I don't understand. Type Yes or No, please: ")
