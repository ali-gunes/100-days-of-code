# This is an exercise for day 16
import random
from turtle import Turtle, Screen, colormode

# We created an object instance from Turtle() class
kepce = Turtle()
my_screen = Screen()
def draw_triangle():
    for i in range(3):
        kepce.forward(100)
        kepce.left(120)

kepce.shape("turtle")
kepce.color("DarkRed")
kepce.shapesize(2)
kepce.pensize(3)


draw_triangle()
kepce.left(180)
draw_triangle()

kepce.home()



my_screen.clearscreen()


# for steps in range(1000):
#     for c in ('blue', 'red', 'green'):
#         kepce.color(c)
#         kepce.forward(steps)
#         kepce.right(30)

# for i in range(500):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     kepce.right(angle)
#     kepce.fd(steps)


# Cool stuff
# my_screen.bgcolor('black')
# x = 1
# kepce.speed(0)
# kepce.pensize(1)
# while x < 400:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     colormode(255)
#     kepce.pencolor(r, g, b)
#     kepce.fd(50 + x)
#     kepce.rt(90.991)
#     x = x + 1

my_screen.exitonclick()

