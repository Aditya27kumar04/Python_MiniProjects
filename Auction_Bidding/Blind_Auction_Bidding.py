import Auction_Art

print(Auction_Art.logo)
print("Welcome to The Silent Auction")


def find_highest_bidder(bids):
    winner = max(bids, key=bids.get)
    print(f"The Winner is {winner} with a bid of ${bids[winner]}.")


bids = {}

while True:
    name = input("What is your name?: ")
    bids[name] = float(input("What is your bid?: $"))

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

    if should_continue == "no":
        find_highest_bidder(bids)
        break

    print("\n" * 20)