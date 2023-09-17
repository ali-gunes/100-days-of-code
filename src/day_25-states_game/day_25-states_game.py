# On day 25, we are: Working with CSV Data and the Pandas Library

# Project 25 - U.S. States Game

from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("Ali G - U.S. State Guessing Game")

player = Turtle()
# player.hideturtle()
player.shape("square")
player.penup()
player.shapesize(stretch_wid=0.25, stretch_len=0.25)
player.speed("slowest")

# I am converting csv data to a list
states_data = pandas.read_csv("50_states.csv")

states_list = list(states_data.state)
states_x = list(states_data.x)
states_y = list(states_data.y)

title = ""
guessed = 0
guessed_list = []
while guessed < 50:
    player_guess = screen.textinput(f"Guessed States: {guessed}/50", "Guess a States Name:").title()

    # For early exit
    if player_guess == "Exit":
        break

    if player_guess in states_list and player_guess not in guessed_list:
        guessed += 1
        guessed_list.append(player_guess)
        state_index = states_list.index(player_guess)
        player.goto(states_x[state_index], states_y[state_index])
        player.write(player_guess)

print(f"Congratulations! You guessed {guessed} states correct!")


# Create a CSV for the user which includes all the states that isn't guessed by the user
mystery_states = []
for states in states_list:
    if states not in guessed_list:
        mystery_states.append(states)

unknown_states = pandas.DataFrame(mystery_states)
unknown_states.to_csv("mystery_states.csv")