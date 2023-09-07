# On day 19, we are: Studying Event Listeners, Multiple Instances, State and Higher Order Functions
# We are also making Etch a Sketch Game and a Turtle Racing Game

# Project 12 - Turtle Racing Game
import turtle as t
import random as r

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = list()

screen = t.Screen()
screen.setup(width=500, height=400)

player_choice = screen.textinput("Choose your Turtle!",
                                 "Which turtle is going to win the race? Enter a color: (red, orange, yellow, green, blue, purple)").lower()

if player_choice not in colors:
    print("You have to choose one of the colors specified. Goodbye.")
    exit()

y_pos = 175

for i in range(6):
    kepce = t.Turtle(shape="turtle")
    kepce.penup()
    kepce.goto(-225, y_pos)
    kepce.color(colors[i])
    y_pos -= 60
    turtles.append(kepce)


def start_race():
    while True:
        for turtle in turtles:
            if turtle.xcor() < 210:
                forward_pace = r.randint(1, 5)
                turtle.forward(forward_pace)
            else:
                return turtle.color()[0]


winner = start_race()

if winner == player_choice:
    print(f"{winner.title()} won! You win!")
else:
    print(f"{winner.title()} won! You lose!")

screen.exitonclick()
