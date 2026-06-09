import random
from Hangman_ASCII_ARTS import Stages, logo
from Hangman_words import word_list

chosen_word = random.choice(word_list)

correct_letters = []
lives = 6
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed '{guess}'. Try another letter!")
        continue

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

    correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        display += letter if letter in correct_letters else "_"

    print(display)
    print(Stages[6 - lives])

    if lives == 0:
        print("You Lose!")
        print(f"The word was: {chosen_word}")
        game_over = True

    elif "_" not in display:
        print("You Win!")
        game_over = True