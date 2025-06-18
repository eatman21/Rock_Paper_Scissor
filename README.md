# 🎮 Rock Paper Scissors Game

A feature-rich command-line implementation of the classic Rock Paper Scissors game in Python with multiple difficulty levels, scoring system, and statistics tracking.

## ✨ Features

- 🎯 **Multiple Difficulty Levels**
  - Easy: Computer is predictable (sometimes copies your moves)
  - Normal: Computer plays randomly
  - Hard: Computer tries to counter your moves (70% smart, 30% random)

- 📊 **Scoring System & Statistics**
  - Real-time score tracking (Wins, Losses, Ties)
  - Win rate calculation
  - Detailed game statistics
  - Session-based scoring

- 🎨 **Enhanced User Experience**
  - Emoji visual feedback (🪨📃✂️)
  - Interactive difficulty selection
  - Clear game instructions
  - Input validation

- 🔄 **Game Controls**
  - `r` - Rock 🪨
  - `p` - Paper 📃
  - `s` - Scissors ✂️
  - `t` - Show statistics 📊
  - `q` - Quit game

## 🚀 How to Play

1. **Run the game:**

   ```bash
   python rosck_paper_scissor.py
   ```

2. **Choose difficulty level:**
   - `1` - Easy (Beginner friendly)
   - `2` - Normal (Balanced gameplay)
   - `3` - Hard (Challenging AI)

3. **Play the game:**
   - Enter your choice when prompted
   - Watch the computer make its move
   - See the result and updated score

4. **Use game commands:**
   - Press `t` anytime to view your statistics
   - Press `q` to quit and see final stats

## 🎯 Game Rules

- **Rock** 🪨 beats **Scissors** ✂️
- **Scissors** ✂️ beats **Paper** 📃
- **Paper** 📃 beats **Rock** 🪨
- Same choices result in a tie 🤝

## 🏆 Difficulty Levels Explained

### Easy Mode

- Computer occasionally copies your previous move
- Great for beginners and learning the game
- Predictable patterns make it easier to win

### Normal Mode

- Computer makes completely random choices
- Classic Rock Paper Scissors experience
- Balanced gameplay for all skill levels

### Hard Mode

- Computer analyzes and tries to counter your moves
- Uses strategic thinking (70% smart, 30% random)
- Challenging for experienced players

## 📊 Statistics Tracking

The game tracks comprehensive statistics:

- **Wins**: Number of games won
- **Losses**: Number of games lost
- **Ties**: Number of tied games
- **Total Games**: Total number of games played
- **Win Rate**: Percentage of games won

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Dependencies**: Only uses Python standard library (`random`)
- **Architecture**: Modular design with separate functions for different game aspects
- **Code Quality**: Uses constants for better maintainability

## 🎨 Code Structure

```python
# Constants for game choices
ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
QUIT = 'q'
STATS = 't'

# Main functions
def get_computer_choice(difficulty, choice)  # AI logic
def display_stats(wins, losses, ties, total) # Statistics display
def game()                                   # Main game loop
```

## 🚀 Future Enhancements

Potential features for future versions:

- [ ] GUI interface using tkinter
- [ ] Sound effects and animations
- [ ] Tournament mode (Best of 3/5/7)
- [ ] High score persistence
- [ ] Multiplayer support
- [ ] Web version using Flask/Django

## 👨‍💻 Author

**eatman21**

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy playing Rock Paper Scissors! 🎮✂️📃🪨**
