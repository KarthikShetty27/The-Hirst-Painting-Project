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

# # color_list for Burnt Sky Image
# color_list = [(149, 84, 35), (239, 147, 79), (30, 52, 77), (61, 75, 88), (254, 217, 180), (253, 185, 123), (50, 62, 81), (79, 69, 74), (218, 113, 32), (251, 254, 254), (81, 88, 85), (212, 106, 48), (254, 253, 254), (251, 253, 254), (64, 55, 60), (70, 60, 65), (70, 54, 49), (82, 57, 51), (40, 69, 85), (99, 60, 25), (254, 178, 130), (44, 51, 50), (140, 145, 156), (150, 147, 149), (55, 69, 66), (156, 158, 155), (189, 192, 197)]

# color_list for the-starry-night Image
# color_list1 = [(71, 94, 132), (23, 33, 55), (127, 150, 176), (26, 33, 29), (38, 54, 108), (34, 32, 26), (147, 165, 152), (98, 123, 168), (169, 174, 128), (87, 101, 93), (98, 100, 71), (158, 151, 66), (201, 204, 147), (32, 27, 30), (196, 212, 199), (189, 208, 225), (115, 136, 124), (213, 217, 187), (108, 135, 142), (72, 75, 38), (180, 199, 183), (55, 69, 61), (167, 187, 224), (48, 69, 75), (85, 80, 83), (175, 198, 203), (69, 60, 64), (73, 59, 57), (155, 151, 153), (131, 127, 126), (131, 126, 133), (206, 204, 206)]

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
