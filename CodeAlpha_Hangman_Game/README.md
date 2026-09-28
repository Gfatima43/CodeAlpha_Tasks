# Hangman Game

A classic command-line Hangman game built in Python. The player tries to guess the hidden word before running out of chances. The game includes a visual hangman progression, word selection from a predefined list, and replay support.

## Features

- Random word selection from a built-in list
- Single-letter guessing input
- Duplicate guess detection
- Wrong guess counter and hangman progression
- Win/lose conditions
- Replay option after each round
- Simple terminal-based interface

## How to Play

1. Open a terminal in the project folder.
2. Run the game with:

```bash
python "hangman_game.py"
```

3. Enter one letter at a time to guess the hidden word.
4. You have 6 wrong guesses before the game ends.
5. After each round, choose whether to play again.

## Game Rules

- Only single alphabetic characters are accepted.
- Repeating a previously guessed letter is not allowed.
- The hidden word is revealed as underscores until correctly guessed.
- A player wins by guessing all letters in the word.
- A player loses if they reach the maximum number of wrong guesses.

## Project Files

- `hangman_game.py` - Main game logic and gameplay loop

## Example Gameplay

```text
WELCOME TO HANGMAN GAME
Guess the hidden word one letter at a time.
You can make 6 incorrect guesses.
Good luck!

Word: _ _ _ _ _ _
Wrong Guesses: 0/6
Guess a letter: p
```

## Requirements

- Python 3.x
