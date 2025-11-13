import random
import sys

wins = 0
losses = 0
topic = None
difficulty = None
secret_word = ""
revealed = []
already_guessed = []
tries = 0

# Helper functions to collect input:
def ask_choice_str(prompt, allowed):

    allowed_lower = [a.lower() for a in allowed]
    allowed_set = set(allowed_lower)

    # validates that the word is one of the choices, reprompts if not
    while True:
        try:
            choice = str(input(prompt).strip().lower())
            if choice in allowed_set:
                return choice
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")

# ---------------TODO-----------------
"""
Random_choice:
1) set up word lists for topic and difficulty
2) initialize word_list as an empty list
3) randomly pick a secret word
4) set up the revealed word list
5) return values
"""

# Word bank for random choice
animal6 = ["monkey", "lizard", "rabbit", "beaver", "badger", "walrus", "iguana"]
animal8 = ["kangaroo", "elephant", "squirrel", "armadillo", "reindeer", "goldfish"]
animal10 = ["chimpanzee", "wildebeest", "timberwolf"]
food6 = ["potato", "tomato", "banana", "carrot", "orange", "cheese"]
food8 = ["eggplant", "pancakes", "macaroni", "sandwich", "cucumber", "zucchini"]
food10 = ["strawberry", "watermelon", "spongecake", "cheesecake", "cornflakes"]
sports6 = ["goalie", "golfer", "hurdle", "league", "player", "soccer", "strike"]
sports8 = ["baseball", "jousting", "football", "swimming"]
sports10 = ["basketball", "gymnastics", "pickleball"]


def random_choice(topic, difficulty):


     word_list = [] # Word list is the list that the secret word will be chosen from
     if topic == "animal":
          if difficulty == "easy":
               word_list = animal6
          elif difficulty == "medium":
               word_list = animal8
          else:
               word_list = animal10
     elif topic == "food":
          if difficulty == "easy":
               word_list = food6
          elif difficulty == "medium":
               word_list = food8
          else:
               word_list = food10
     elif topic == "sports":
          if difficulty == "easy":
               word_list = sports6
          elif difficulty == "medium":
               word_list = sports8
          else:
               word_list = sports10

     secret_word = random.choice(word_list)     # secret_word is the word that the player has to guess
     revealed = ['_'] * len(secret_word)       # revealed is the  list of correctly guessed letters in the right order, with unknown letters as underscores

     return secret_word, revealed

#--------------TODO-------------------
"""
Guess Validator:
Validates that the letter guessed is one letter
1) if the letter is valid, return the letter
2) if the letter is not valid, return None
"""

def guess_validator(letter_guess_input):


     letter_guess = letter_guess_input.strip().lower()
     if len(letter_guess) == 1 and letter_guess.isalpha():
          return letter_guess
     else:
          return None # Indicate invalid input

#----------------TODO----------------------
"""
Guess Tracker:
Tracks the letters guessed to make sure there are no repeats
Processes the letter guessed, updates tries, and reveal respective letters
1) if the new guess is in already_guessed, print a warning message and reprompt
2) Otherwise, add it to already_guessed
3) if the new guess is in the secret word, print success message, reveal letters
4) If the new guess is not in the secret word, print message, reduce tries by one
5) return values
"""

def guess_tracker(letter_guess, tries, revealed, secret_word, already_guessed):


     if letter_guess in already_guessed:
          print("You have guessed this letter already. Pick a new letter.")
     else:
          already_guessed.append(letter_guess)
          already_guessed.sort()

          if letter_guess in secret_word:
               # reveal_letter returns a new list, so revealed can be reassigned
               revealed = reveal_letter(letter_guess, revealed, secret_word)
               print(f"Letter '{letter_guess}' is in the secret word!")
          else:
               print(f"Letter '{letter_guess}' is not in the secret word.")
               tries -= 1

     return tries, revealed, already_guessed

# -------------------TODO--------------------
"""
Reveal letter:
Reveals all locations of the letter guessed in the secret word
1) for each match in the secret word, replace the underscore with the letter
2) return the new revealed word
"""

def reveal_letter(letter_guess, revealed_list, secret_word_val):


     for i in range(len(secret_word_val)):
          if secret_word_val[i] == letter_guess:
               revealed_list[i] = letter_guess
     return revealed_list # Return the modified list

# ----------------------TODO-------------------------
"""
Display progress:
Displays the current progress at the beginning of each turn
1) prints revealed word so far
2) print remaining tries
3) print salready_guessed letter
"""

def display_progress(revealed_word, tries_left, guessed_letters):


     print(f"Your progress: {' '.join(revealed_word)}")
     print(f"Tries left: {tries_left}")
     print(f"Already guessed: {', '.join(sorted(guessed_letters))}\n")

# -------------------------TODO------------------------
"""
End game win:
1) add one win to wins
2) print success message
3) print record
4) ask if they want to play again
    A) if the answer is yes, the loop will restart
    B) if the answer is no, exit the program
5) return wins and losses
"""

def end_game_win(current_wins, current_losses):


     global wins
     global losses
     wins = current_wins + 1
     losses = current_losses
     print("\nCongratulations! You won the game!")
     print(f"Your record is {wins} wins and {losses} losses.")
     play_again = ask_choice_str("Do you want to play again? (y/n)", ["y", "n"])
     if play_again == 'n':
          print("Thank you for playing! Goodbye!")
          sys.exit(0)
     return wins, losses

#--------------------TODO-----------------------------
"""
End game loss:
1) add one loss to losses
2) print failure message
3) print what the secret word was
4) print record
5) ask if they want to play again
    A) if the answer is yes, the loop will restart
    B) if the answer is no, exit the program
5) return wins and losse
"""
def end_game_loss(current_wins, current_losses, secret_word_val):


     global wins
     global losses
     wins = current_wins
     losses = current_losses + 1 # Still using global wins/losses for now, will refactor later
     print("\nYou are out of tries. You lose.")
     print(f"The mystery word was: {secret_word_val}")
     print(f"Your record is {wins} wins and {losses} losses.")
     play_again = ask_choice_str("Do you want to play again? (y/n)", ["y", "n"])
     if play_again == 'n':
          print("Thank you for playing! Goodbye!")
          sys.exit(0)
     return wins, losses

# -----------------------TODO---------------------
"""
Start game:
1) initialize already_guessed and tries
2) ask for topic
3) ask for difficulty
4) Call random_choice and assign its return values
5) return game variables
"""

def start_game():


     already_guessed = []
     tries = 6

     topic = ask_choice_str("Pick a topic: [animal/ food/ sports] ", ["animal", "food", "sports"])
     difficulty = ask_choice_str("Pick a difficulty: [easy/medium/hard] ", ["easy", "medium", "hard"])

     # Call random_choice and assign its return values
     secret_word, revealed = random_choice(topic, difficulty)

     # return game variables
     return secret_word, revealed, already_guessed, tries


# ----------------------TODO--------------------------
"""
Your turn:
1) start loop:
    A) ask for a letter guess
    B) call guess_validator
2) if the letter guess is valid:
    A) call guess tracker
    B) return values
3) otherwise, warn and reprompt
"""

def your_turn(current_tries, current_revealed, current_secret_word, current_already_guessed):


    while True:
        letter_guess_input = input("Enter a letter: ")
        letter_guess_validated = guess_validator(letter_guess_input)
        if letter_guess_validated:
            # Pass all necessary variables to guess_tracker and receive updated variables
            updated_tries, updated_revealed, updated_already_guessed = \
                guess_tracker(letter_guess_validated, current_tries, current_revealed, current_secret_word, current_already_guessed)
            return updated_tries, updated_revealed, updated_already_guessed # Return updated state
        else:
            print("Invalid input. Please enter a single letter.")

# -----------------------TODO------------------------
"""
Main:
1) print welcome message
2) make wins and losses global
3) start outer loop for playing multiple games
4) start inner loop for individual games
5) call your_turn
6) check for game conditions:
    A) if there are no tries left end_game_loss
    B) break out of inner loop
    C) otherwise if there are no underscores left end_game_win
    D) break out of inner loop
"""

def main():


    print("Welcome to Guess the Word!")
    global wins, losses # Keep global wins/losses for now as per original code setup
    while True: # Outer loop for playing multiple games
        secret_word, revealed, already_guessed, tries = start_game()

        while True: # Inner loop for a single game
            display_progress(revealed, tries, already_guessed)

            # Call your_turn
            tries, revealed, already_guessed = your_turn(tries, revealed, secret_word, already_guessed)

            # Check for game end conditions after each turn
            if tries == 0:
                wins, losses = end_game_loss(wins, losses, secret_word)
                break # Break from the inner game round loop
            elif "_" not in revealed: # Check if all letters are revealed
                wins, losses = end_game_win(wins, losses)
                break

# call main
main()