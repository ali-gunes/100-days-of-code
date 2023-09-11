from turtle import Turtle


# 40px for each lane, 10-10 buffer, 20px car width
# Total of 10 lanes: 200, -200

class Lanes(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(3)
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.goto(0, 230)
        self.write("Finish Line", move=False, align="center", font=("Arial", 16, "bold"))
        self.goto(0, 220)
        self.write("-----------------", move=False, align="center", font=("Arial", 16, "bold"))
        self.goto(-500, 200)

    def draw_lanes(self):
        for lane in range(11):
            while self.xcor() <= 500:
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)

            # Go to next line
            self.goto(-500, self.ycor() - 40)
