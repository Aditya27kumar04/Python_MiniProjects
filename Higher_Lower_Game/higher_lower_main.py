import random
from art import logo, vs
from Question_lists import data


def format_data(account):
    """Takes the account data and returns a printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    print(logo)
    score = 0
    game_should_continue = True

    # Generate a random account from the game data for position A
    account_a = random.choice(data)
    # Generate position B
    account_b = random.choice(data)

    # Make the game repeat
    while game_should_continue:
        # Ensuring account_a and account_b are never the exact same account
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Give feedback and update score
        if is_correct:
            score += 1
            print(f"\nYou're right! Current score: {score}.\n")
            # Account B becomes the new Account A for the next round
            account_a = account_b
            account_b = random.choice(data)
        else:
            game_should_continue = False
            print(f"\nSorry, that's wrong. Final score: {score}.")


# Run the game
if __name__ == "__main__":
    play_game()