import random
from Art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculate the score of a hand."""

    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace from 11 to 1 if score exceeds 21
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"

    elif user_score == 0:
        return "You win with a Blackjack!"

    elif computer_score == 0:
        return "You lose. Opponent has Blackjack!"

    elif user_score > 21:
        return "You went over. You lose."

    elif computer_score > 21:
        return "Opponent went over. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose!"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial two cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            should_deal = input(
                "Type 'yes' to get another card, type 'no' to pass: "
            ).lower()

            if should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    computer_score = calculate_score(computer_cards)

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("\n===== FINAL RESULT =====")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Main game loop
while input("\nDo you want to play Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    print("\n" * 20)

    play_game()