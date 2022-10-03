# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_painting.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
color_list = [(239, 236, 232), (237, 239, 243), (242, 237, 239), (233, 240, 236), (206, 151, 94), (40, 98, 145), (209, 211, 112), (132, 171, 200), (152, 61, 86), (158, 77, 48), (62, 120, 67), (129, 183, 154), (204, 84, 105), (214, 89, 61), (196, 130, 156), (13, 48, 87), (181, 149, 50), (135, 34, 46), (72, 44, 32), (35, 60, 41), (30, 60, 117), (207, 215, 16), (123, 41, 35), (39, 167, 136), (31, 85, 51), (155, 205, 213), (158, 207, 191), (37, 172, 181), (223, 174, 185), (77, 38, 43)]


tim.setheading(225)
tim.forward(300)
tim.setheading(00)

numer_of_dots = 100

for dot_count in range(1, numer_of_dots + 1):
    tim.forward(50)
    tim.dot(20, random.choice(color_list))

    if dot_count % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()