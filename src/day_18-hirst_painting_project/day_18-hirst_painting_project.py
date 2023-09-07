# On day 18, we are: Studying the Turtle module and GUI

# Project 18 - Hirst Painting Project

import turtle as t
import random

hirst = t.Turtle()
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)


def start_position(x=-150, y=-150):
    hirst.shape("square")
    hirst.shapesize(.1, .1, .1)
    hirst.penup()
    hirst.setx(x)
    hirst.sety(y)


def draw_circle():
    hirst.pendown()
    hirst.speed("fastest")
    hirst.color(random_color())
    hirst.begin_fill()
    hirst.circle(10)
    hirst.end_fill()
    hirst.speed("normal")
    hirst.penup()


def complete_canvas(dot_number=100, row_num=10):
    start_position()

    line_dots = int(dot_number / row_num)
    y = int(hirst.xcor())
    for _ in range(line_dots):
        y += 30
        start_position(y=y)
        for dot in range(int(line_dots)):
            draw_circle()
            hirst.forward(30)


complete_canvas()

screen = t.Screen()
screen.exitonclick()
