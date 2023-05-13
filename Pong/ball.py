from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_movement = 10
        self.x_movement = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.7

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.y_movement *= -1
        self.x_movement *= -1
