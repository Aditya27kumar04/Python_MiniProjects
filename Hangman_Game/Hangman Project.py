import random
from Hangman_ASCII_ARTS import Stages, logo
from Hangman_words import word_list



print(logo)

chosen_word = random.choice(word_list)
print(f" The word is: {chosen_word}")

correct_letters = []
lives = 6
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # REPEAT GUESS PROTECTION
    if guess in correct_letters:
        print(f"You already guessed '{guess}'. Try another letter!")
        continue

    correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # WRONG guess = lose life
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

    # Print the stage AFTER updating lives
    print(Stages[6 - lives])

    # Lost all lives.
    if lives == 0:
        print("You Lose!")
        print(f"The word was: {chosen_word}")
        game_over = True

    # Guessed whole word
    if "_" not in display:
        print("You Win!")
        game_over = True