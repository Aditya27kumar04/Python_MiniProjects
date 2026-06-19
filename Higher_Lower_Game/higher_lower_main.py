# ----------------------------------------------------------
# Higher Lower Game
# Compare two celebrities and guess who has more followers.
# Built using Python.
# ----------------------------------------------------------

import random
from art import logo, vs
from Question_lists import data


def format_data(account):
    """
    Takes the account data and returns it in a printable format.
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def check_answer(user_guess, a_followers, b_followers):
    """
    Returns True if the user's guess is correct.
    """
    if a_followers > b_followers:
        return user_guess == "a"
    return user_guess == "b"


print(logo)

score = 0
game_should_continue = True

# Generate the first account
account_a = random.choice(data)

while game_should_continue:

    # Make B become the next A
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["value"]
    b_followers = account_b["value"]

    is_correct = check_answer(
        guess,
        a_followers,
        b_followers
    )

    if is_correct:
        score += 1
        print("\n" * 20)   # Simulates clearing the screen
        print(logo)
        print(f"✅ Correct! Current score: {score}\n")

        # Move B to A for the next round
        account_a = account_b

    else:
        print(f"\n❌ Sorry, that's wrong.")
        print(f"Final Score: {score}")
        game_should_continue = False