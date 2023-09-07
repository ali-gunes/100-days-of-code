# On day 19, we are: Studying Event Listeners, Multiple Instances, State and Higher Order Functions
# We are also making Etch a Sketch Game and a Turtle Racing Game

# Project 12 - Etch a Sketch Game

# We need to listen user's keyboard strokes with event listeners
import turtle as t

kepce = t.Turtle()
screen = t.Screen()


def move_forward():
    kepce.forward(10)


def move_backward():
    kepce.backward(10)


def turn_left():
    kepce.left(10)


def turn_right():
    kepce.right(10)


def pen_up():
    kepce.penup()

def pen_down():
    kepce.pendown()

screen.listen()
# We didn't add paranthesis for the function
# Adding paranthesis when passing a function to a function will trigger for execution
# right there instead of with condition. Below, you can see onkey() or onkeypress() is the higher order function.
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=pen_up, key="q")
screen.onkey(fun=pen_down, key="e")

screen.exitonclick()
