import random as ra

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
QUIT = 'q'
STATS = 't'

emoji_map = {
    ROCK: '🪨',
    PAPER: '📃',
    SCISSOR: '✂️'
}


choise = tuple(emoji_map.keys())


def get_computer_choice(difficulty, choice):
    """Get computer choice based on difficulty level"""
    if difficulty == 'easy':
        # Easy: mostly random, sometimes predictable
        if ra.random() < 0.3:
            return choice  # Computer copies player
        return ra.choice(choice)
    elif difficulty == 'hard':
        # Hard: tries to predict and counter player
        if ra.random() < 0.7:
            # Counter the most likely player choice
            counters = {ROCK: PAPER, PAPER: SCISSOR, SCISSOR: ROCK}
            return counters[ra.choice(choice)]
        return ra.choice(choice)
    else:
        # Normal: completely random
        return ra.choice(choice)


def display_stats(wins, losses, ties, total_games):
    """Display game statistics"""
    print(f"\n📊 GAME STATISTICS:")
    print(f"Wins: {wins} | Losses: {losses} | Ties: {ties}")
    print(f"Total Games: {total_games}")
    if total_games > 0:
        win_rate = (wins / total_games) * 100
        print(f"Win Rate: {win_rate:.1f}%")
    print("-" * 30)


def game():
    choise = (ROCK, PAPER, SCISSOR)
    wins = losses = ties = 0

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Choose difficulty level:")
    print("1. Easy (Computer is predictable)")
    print("2. Normal (Computer is random)")
    print("3. Hard (Computer is smart)")

    while True:
        difficulty_input = input("Enter difficulty (1/2/3): ").strip()
        if difficulty_input == '1':
            difficulty = 'easy'
            break
        elif difficulty_input == '2':
            difficulty = 'normal'
            break
        elif difficulty_input == '3':
            difficulty = 'hard'
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print(f"\n🎯 Difficulty: {difficulty.upper()}")
    print("Let's play! Enter 'q' to quit, 't' to see stats\n")

    while True:  # loop to play again
        user_choise = input('Rock, Paper, Scissor? (r/p/s/q/t): ').lower()

        if user_choise == 'q':
            print("Thanks for playing!")
            display_stats(wins, losses, ties, wins + losses + ties)
            break
        elif user_choise == STATS:
            display_stats(wins, losses, ties, wins + losses + ties)
            continue
        elif user_choise not in choise:
            print("Invalid choice. Please try again.")
            continue

        computer_choise = get_computer_choice(difficulty, choise)
        print(
            f"\nYou chose {emoji_map[user_choise]}, computer chose {emoji_map[computer_choise]}")

        if user_choise == computer_choise:
            print("🤝 It's a tie!")
            ties += 1
        elif (
            (user_choise == ROCK and computer_choise == SCISSOR) or
            (user_choise == PAPER and computer_choise == ROCK) or
                (user_choise == SCISSOR and computer_choise == PAPER)):
            print("🎉 You win!")
            wins += 1
        else:
            print("😔 You lose!")
            losses += 1

        print(f"Score: You {wins} - Computer {losses} - Ties {ties}\n")


if __name__ == "__main__":
    game()
