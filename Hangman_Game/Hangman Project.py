import random

Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

chosen_word = random.choice(word_list)
print(f" The word is: {chosen_word}")

correct_letters = []
lives = 6
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess not in correct_letters:
        correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # WRONG guess → lose life FIRST
    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess!")

    # Print the stage AFTER updating lives
    print(Stages[6 - lives])

    # When Lost all lives.
    if lives == 0:
        print("You Lose!")
        print(f"The word was: {chosen_word}")
        game_over = True

    # Guessed word
    if "_" not in display:
        print("You Win!")
        game_over = True
