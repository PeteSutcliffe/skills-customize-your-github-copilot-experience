
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Python Hangman game that uses loops, conditionals, and user input to let players guess a hidden word before they run out of attempts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a Hangman game that randomly selects a word and displays progress as the player guesses letters.

#### Requirements
Completed program should:

- Use a predefined list of words and choose one at random
- Display the current word progress with blanks and revealed letters
- Accept letter guesses from the user
- Track letters already guessed

### 🛠️ Guess Handling and Game Logic

#### Description
Implement the core game loop so the player can keep guessing until they win or lose.

#### Requirements
Completed program should:

- Deduct remaining attempts for incorrect guesses
- End the game when the word is guessed or attempts are exhausted
- Show a win message when the player guesses the word
- Show a lose message and reveal the word if attempts run out

### 🛠️ User Experience and Feedback

#### Description
Add clear feedback for the player after each guess so they can follow the game state.

#### Requirements
Completed program should:

- Display the current progress after each guess
- Show how many incorrect guesses remain
- Prevent repeated guesses from using extra attempts
- Use friendly messages for correct, incorrect, win, and lose outcomes
