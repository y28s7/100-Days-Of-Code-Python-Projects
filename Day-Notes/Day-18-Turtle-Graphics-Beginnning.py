# TODO 1: Draw a square
# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# tim.shape("triangle")
# tim.color("cyan")
# for num in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# screen = Screen()
# screen.exitonclick()

# TODO 2: Draw a dashed line
# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# tim.shape("triangle")
# tim.color("cyan")
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#
# screen = Screen()
# screen.exitonclick()

# TODO 3: Draw a multitude of shapes
# from turtle import Turtle, Screen
# from random import choice
#
# tim = Turtle()
#
# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
#
# tim.shape("triangle")
# tim.color("cyan")
#
# for sides in range(3, 11):
#     tim.pencolor(choice(colors))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)
#
# screen = Screen()
# screen.exitonclick()

# TODO 4: Make a random walk
# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# directions = [0, 90, 180, 270]
#
# tim.shape("triangle")
# tim.color("cyan")
# tim.speed("fastest")
# tim.pensize(10)
#
# for _ in range(200):
#     tim.setheading(random.choice(directions))
#     tim.pencolor(random_color())
#     tim.fd(25)
#
# screen = t.Screen()
# screen.exitonclick()

# TODO 5: Make a spirograph
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.shape("triangle")
tim.color("cyan")
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
