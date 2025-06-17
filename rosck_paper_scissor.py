import random as ra


def game():
    user = input("Enter a choice (r for rock, p for paper, s for scissor): ")
    if user == "r":
        user = "rock"
    elif user == "p":
        user = "paper"
    elif user == "s":
        user = "scissor"
    computer = ra.choice(["rock", "paper", "scissor"])
    if computer == "r":
        computer = "rock"
    elif computer == "p":
        computer = "paper"
    elif computer == "s":
        computer = "scissor"
    print(f"You chose {user}, computer chose {computer}")

    if user == computer:
        return "It's a tie!"
    elif user == "rock":
        if computer == "scissor":
            return "You win!"
        else:
            return "You lose!"
    elif user == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif user == "scissor":
        if computer == "paper":
            return "You win!"
        else:
            print("You lose!")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                return game()
            else:
                return "Thanks for playing!"


if __name__ == "__main__":
    while True:
        result = game()
        print(result)
        if result == "Thanks for playing!":
            break
