# # Task 04: Number Guessing Game

# ## Objective

# Create a simple number guessing game where the program generates a random number, and the user has to guess it.
    
# ## Requirements

# 1. Generate a random number between a specified range.
# 2. Ask the user to guess the number.
# 3. Provide feedback on whether the guess is too high, too low, or correct.
# 4. Allow the user to continue guessing until they guess the correct number.
# 5. Display the number of attempts it took to guess correctly.

# ## Additional Challenges

# 1. Implement error handling to ensure the user inputs a valid number.
# 2. Allow the user to choose the range of numbers for the guessing game.
# 3. Enhance the program to provide hints or clues based on the user's previous guesses.
import random
print("Welcome to number guessing game!!!")
print("Choose the range of numbers you want to guess!!")
starting = int(input("Enter starting range:"))
ending = int(input("Enter ending number:"))

random_number = random.randint(starting, ending)
# print("randomnumber",random_number)
print("Guess the number!!!")

correct = True
attempt = 0
while correct:
    num = int(input(f"Guess the number between {starting} and {ending}: "))
    if num > ending or num < starting:
        print(f"Please enter the number between {starting} and {ending}.")
    elif num > random_number:
        print("Too high")
        attempt += 1
    elif num < random_number:
        print("Too low")
        attempt += 1
    elif num == random_number:
        print(f"You've guessed the right number, You've guess the number in {attempt} attempt.")
        correct = False

