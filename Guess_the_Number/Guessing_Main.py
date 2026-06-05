from Art import logo
print(logo)

from random import randint

print("Welcome to the Number Guessing Game")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("I am Thinking of a number between 1 and 100.")
answer = randint(1, 100)

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function to check user's guess against actual number
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too High!")
    elif user_guess < actual_answer:
        print("Too Low!")
    else:
        print(f"You guessed it correctly! The answer is {actual_answer}")

turns = set_difficulty()
guess = 0

while guess != answer and turns > 0:
    print(f"\nYou have {turns} attempts remaining.")

    guess = int(input("Make a guess: "))
    check_answer(guess, answer)

    if guess != answer:
        turns -= 1

if turns == 0:
    print(f"You've run out of guesses. The answer was {answer}.")