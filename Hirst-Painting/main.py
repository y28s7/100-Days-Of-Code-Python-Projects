# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

import turtle as t
from random import choice

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.left(180)
tim.fd(250)
tim.left(90)
tim.fd(250)
tim.setheading(0)

for _ in range(10):
    for num in range(10):
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

