from Art import logo
print(logo)

from random import randint

print("Welcome to the Number Guessing Game")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("I am thinking of a number between 1 and 100.")
answer = randint(1, 100)

# Set difficulty level
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Check the guess
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high!")
        return False

    elif user_guess < actual_answer:
        print("Too low!")
        return False

    else:
        print(f"You got it! The answer was {actual_answer}.")
        return True


turns = set_difficulty()
game_over = False

while not game_over and turns > 0:

    print(f"\nYou have {turns} attempts remaining.")

    guess = int(input("Make a guess: "))

    result = check_answer(guess, answer)

    if result:
        game_over = True
    else:
        turns -= 1

        if turns > 0:
            print("Guess again.")

if turns == 0:
    print(f"You've run out of guesses. The answer was {answer}.")