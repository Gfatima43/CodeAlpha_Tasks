import random

# Words available for the game to choose from.
words = ["python", "developer", "database", "computer", "programming"]

separator_width = 50

# Each picture represents the hangman after a different number of wrong guesses.
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

# Word display and guess-validation helpers.
def create_display_word(word, guessed_letters):
    display_word = ""
    for letter in word:
        display_letter = letter if letter in guessed_letters else "_"
        display_word += display_letter + " "
    return display_word.strip()

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def is_duplicate_guess(guess, guessed_letters):
    return guess in guessed_letters

def is_correct_guess(guess, word):
    return guess in word

def has_won(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def is_game_over(wrong_guesses, max_wrong_guesses):
    return wrong_guesses >= max_wrong_guesses

def can_continue(wrong_guesses, max_wrong_guesses):
    return wrong_guesses < max_wrong_guesses

# Messages and visuals used while a round is in progress.
def get_guess_word(guesses_left):
    return "guess" if guesses_left == 1 else f"You have {guesses_left} guesses left."

def get_hangman_pic(wrong_guesses):
    idx = min(wrong_guesses, len(HANGMAN_PICS) - 1)
    return HANGMAN_PICS[idx]

# Screen messages shown before and after each round.
def show_welcome():
    print("=" * separator_width)
    print("           WELCOME TO HANGMAN GAME")
    print("=" * separator_width)
    print("Guess the hidden word one letter at a time.")
    print("You can make 6 incorrect guesses.")
    print("Good luck!\n")
    
def show_round_start():
    print("\n" + "-" * separator_width)
    print("              Starting a new round...")
    print("-" * separator_width)
    
def show_goodbye():
    print("\n" + "=" * separator_width)
    print("              THANKS FOR PLAYING HANGMAN!")
    print("                  See you next time!")
    print("=" * separator_width)
    
def ask_to_play_again():
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def play_game():
    # Reset the state so every round starts with a new word and no guesses.
    show_round_start()
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    while can_continue(wrong_guesses, max_wrong_guesses):
        # Show the current progress before asking for the next guess.
        print(get_hangman_pic(wrong_guesses))
        print(f"\nWord: {create_display_word(word, guessed_letters)}")
        print(f"Wrong Guesses: {wrong_guesses}/{max_wrong_guesses}")
        guess = input("Guess a letter: ").strip().lower()
        
        if not is_valid_guess(guess):
            print("Please enter a single letter.")
            continue
        
        if is_duplicate_guess(guess, guessed_letters):
            print("You already guessed that letter.")
            continue
        
        # Store valid guesses once so they are revealed in the displayed word.
        guessed_letters.append(guess)
        
        if not is_correct_guess(guess, word):
            wrong_guesses += 1
            guesses_left = max_wrong_guesses - wrong_guesses
            guess_word = get_guess_word(guesses_left)
            print(f"Wrong guess! You have {guesses_left} {guess_word}")
            
        # Check for a win after each new, valid guess.
        if has_won(word, guessed_letters):
            print(get_hangman_pic(wrong_guesses))
            print("=" * separator_width)
            print(f"Congratulation! \nYou've guessed the word: {word}")
            print("=" * separator_width)
            return
        
    if is_game_over(wrong_guesses, max_wrong_guesses):
        print(get_hangman_pic(wrong_guesses))
        print("=" * separator_width)
        print(f"Game Over! \nThe word was: {word}")
        print("=" * separator_width)    
        
# Start the first round, then repeat only when the player requests it.
show_welcome()

while True:
    play_game()
    if not ask_to_play_again():
        show_goodbye()
        break