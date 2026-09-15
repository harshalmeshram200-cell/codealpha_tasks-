 import random

# List of 5 predefined words
words = ["python", "computer", "science", "program", "coding"]

# Randomly select a word
word = random.choice(words)

# Create a list to store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
incorrect_guesses = 0

print("=" * 40)
print("        WELCOME TO HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses available.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the current state of the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! 🎉")
        print("You guessed the word:", word)
        break

    # Take input from the player
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess! ✅\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌\n")

# Game over condition
else:
    print("\n" + "=" * 40)
    print("GAME OVER! 😢")
    print("The correct word was:", word)
    print("=" * 40)