# import colorgram
import random
import turtle as t
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

t.colormode(255)
color_list = [(208, 157, 105), (228, 241, 238), (58, 98, 132), (156, 83, 53), (139, 159, 189), (231, 202, 104), (158, 167, 41), (52, 174, 121), (122, 189, 173), (201, 136, 154), (65, 39, 32), (76, 113, 88), (126, 80, 88), (133, 30, 48), (28, 48, 67), (195, 93, 74), (181, 93, 110)]
timmy = t.Turtle()



def generate_random_color(c_list):
    return random.choice(c_list)

timmy.teleport(-200, -200)
start_x = timmy.xcor()
start_y = timmy.ycor()
timmy.hideturtle()

def set_y_coordinate(turtle):
    y_cord = turtle.ycor()
    return y_cord + 50

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, generate_random_color(color_list))
        timmy.pu()
        timmy.fd(50)

    timmy.teleport(start_x, set_y_coordinate(timmy))

my_screen = t.Screen()
print(my_screen.window_width())
print(my_screen.window_height())
my_screen.exitonclick()