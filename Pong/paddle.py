from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(position)
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
