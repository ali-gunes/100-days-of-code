from turtle import Turtle, Screen, colormode
import random  # To change pen's color

hirst_turtle = Turtle()
hirst_turtle.shape("square")


def draw_square():
    for _ in range(4):
        hirst_turtle.forward(100)
        hirst_turtle.left(90)


def dashed_line():
    for _ in range(10):
        hirst_turtle.forward(10)
        hirst_turtle.penup()
        hirst_turtle.forward(10)
        hirst_turtle.pendown()

    hirst_turtle.left(72)


def draw_sequence():
    colormode(255)
    hirst_turtle.pensize(2)
    # 3 - 4 - 5: (Line number - 2) * 180 = Sum of Inner Angles
    n = 3  # Start with triangle
    while n <= 11:
        hirst_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # Random color
        turn_angle = 360 / n
        # hirst_turtle.begin_fill()
        for _ in range(n):
            hirst_turtle.forward(100)
            hirst_turtle.left(turn_angle)
        # hirst_turtle.end_fill()
        n += 1


def random_walk():
    hirst_turtle.pensize(10)
    colormode(255)
    position_traveled = 0
    hirst_turtle.speed(10)
    for i in range(200):
        # We use tuple for color method
        hirst_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        forward_distance = random.randint(1, 50)
        hirst_turtle.forward(forward_distance)
        position_traveled += forward_distance
        hirst_turtle.left(random.choice([90, 180, 270, 360]))
        if hirst_turtle.xcor() <= -295 or hirst_turtle.xcor() >= 295:
            print("Warning! Turtle is trying to escape!\nTeleporting it to start!")
            hirst_turtle.setposition(0, 0)
        elif hirst_turtle.ycor() <= -295 or hirst_turtle.ycor() >= 295:
            print("Warning! Turtle is trying to escape!\nTeleporting it to start!")
            hirst_turtle.setposition(0, 0)
        print(f"Position traveled: {position_traveled} meters.")
        print(f"Total displacement: {round(hirst_turtle.distance(0, 0), 2)} meters.\n")


def spirograph():
    hirst_turtle.speed(0)
    colormode(255)
    gap_degree = 1
    for _ in range(int(360 / gap_degree)):
        # I liked it black
        # hirst_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        hirst_turtle.circle(150)
        hirst_turtle.left(gap_degree)

# draw_square()
# for _ in range(5):
#     dashed_line()
# draw_sequence()
# random_walk()
# spirograph()

screen = Screen()
screen.exitonclick()
