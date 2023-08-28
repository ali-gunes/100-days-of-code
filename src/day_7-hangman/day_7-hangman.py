# On day 7, we are: Reviewing For/While Loops, If/Elif/Else Conditions, Lists, Strings, Range, and Modules

# Project 7 - Hangman
import random
import hangman_words
import hangman_art

# Step 1
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Step 2
# TODO-4 - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
#  So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter
#  to guess.
# TODO-5 - Loop through each position in the chosen_word;
#   If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#   e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Step 3
# TODO-6 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
#   all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# Step 4
# TODO-7 - Create a variable called 'lives' to keep track of the number of lives left.
#   Set 'lives' to equal 6.
# TODO-8 - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
#   If lives goes down to 0 then the game should stop and it should print "You lose."
# TODO-9 - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
display = []
guessed_letters = []
user_lives = 6
end_of_game = False
for char in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter:\t").lower()
    word_index = 0

    for char in chosen_word:
        if guess == char:
            display[word_index] = guess
            if guess in guessed_letters:
                print("You've already guessed this letter, try another one.")
            guessed_letters.append(guess)
        word_index += 1

    if guess not in chosen_word:
        if guess not in guessed_letters:
            user_lives -= 1
            print(hangman_art.stages[user_lives])
            guessed_letters.append(guess)
            print(f"You guessed '{guess}', that's not in the word. You lose a life!")
        else:
            print("You've already tried this letter, you didn't lose any lives.")

    print(f"{''.join(display)}")  # Concatenate string list into a string

    if "_" not in display:
        # This means user won
        end_of_game = True
        print("\n\nCongratulations! You win!")

    if user_lives == 0:
        # This means user lost
        end_of_game = True
        print("\n\nYou are out of lives, your little man is hanged. You lose!")
        print("The word was:\t", chosen_word)
