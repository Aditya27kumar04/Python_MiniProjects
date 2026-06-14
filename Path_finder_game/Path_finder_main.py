from art import logo
print(logo)
print("Welcome to Secret Treasure Hunt!")
print("Your mission is to find the hidden treasure.")

choice1 = input("You are at the entrance of a cave. Go Left or Right? ").lower()

if choice1 == "left":

    choice2 = input(
        "You find an underground river. Swim or Build a Raft? ").lower()

    if choice2 == "raft":

        choice3 = input(
            "You reach a chamber with three doors. Red, Blue, or Green? ").lower()

        if choice3 == "green":
            print("Congratulations!")
            print("You found the treasure chest full of gold!")
            print("You Win!")

        elif choice3 == "red":
            print("The red door triggered a fire trap.")
            print("Game Over.")

        elif choice3 == "blue":
            print("A giant monster was waiting behind the blue door.")
            print("Game Over.")

        else:
            print("That door does not exist.")
            print("Game Over.")

    elif choice2 == "swim":
        print("The river current was too strong.")
        print("Game Over.")

    else:
        print("Invalid choice.")
        print("Game Over.")

elif choice1 == "right":
    print("You entered a cave full of bats.")
    print("Game Over.")

else:
    print("Invalid choice.")
    print("Game Over.")