import random as ra

emoji_map = {
    'r': '🪨',
    'p': '📃',
    's': '✂️'
}


def game():
    choise = ('r', 'p', 's')
    while True:  # loop to play again
        print("Welcome to Rock, Paper, Scissor!")
        user_choise = input('Rock, Paper, Scissor? (r/p/s): ').lower()
        if user_choise not in choise:
            print("Invalid choice. Please try again.")
            continue
        computer_choise = ra.choice(choise)
        print(
            f"You chose {emoji_map[user_choise]}, computer chose {emoji_map[computer_choise]}")

        if user_choise == computer_choise:
            print("It's a tie!")
        elif (
            (user_choise == 'r' and computer_choise == 's') or
            (user_choise == 'p' and computer_choise == 'r') or
                (user_choise == 's' and computer_choise == 'p')):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    game()
