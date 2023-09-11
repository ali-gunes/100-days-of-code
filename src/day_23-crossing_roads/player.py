from turtle import Turtle


# Screen size: 1000, 600

class Player(Turtle):  # Inherit from Turtle class
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, -250)
        self.setheading(90)
        self.shape("turtle")

    def move(self):
        """
        Move forward with space bar
        """
        if self.ycor() < 280:
            self.forward(10)
