# On day 4, we are: Studying Randomisation and Python Lists

# Project 4 - Rock Paper Scissors Game
import random

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\t"))
computer_choice = random.randint(0, 2)

# Ascii Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_list = [rock, paper, scissors]

# Note that I just didn't add if conditions blindly, I tried to cover base cases and added elif statements for
# edge-cases, thus reduced the number of if conditions required

if human_choice >= 3 or human_choice < 0:
    print("You typed an invalid option, you lose!")
    exit()

print("You chose:")
print(ascii_list[human_choice])
print("Computer chose:")
print(ascii_list[computer_choice])

if human_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and human_choice == 2:
    print("You lose!")
elif computer_choice > human_choice:
    print("You lose")
elif human_choice > computer_choice:
    print("You win!")
elif computer_choice == human_choice:
    print("It's a draw!")
