# # To extract the colors from a picture
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('1.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# print(len(rgb_colors))


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed = ('fast')
tim.hideturtle()
tim.penup()

# color_list for 1 Image
color_list2 = [(64, 88, 146), (46, 46, 121), (23, 32, 79), (141, 66, 109), (122, 29, 81), (63, 23, 64), (168, 85, 48), (187, 130, 148), (182, 90, 119), (206, 131, 87), (76, 124, 104), (206, 94, 66), (96, 108, 174), (91, 149, 118), (202, 128, 38), (108, 144, 174), (109, 163, 131), (79, 145, 159), (110, 46, 39), (27, 77, 94), (74, 48, 42), (41, 62, 59), (40, 80, 71), (220, 167, 182), (69, 65, 54), (224, 171, 165), (227, 196, 93), (179, 204, 223), (185, 186, 207)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list2))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
