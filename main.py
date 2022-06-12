
import turtle as turtle_module
import random
turtle_module.colormode(255)
rue = turtle_module.Turtle()
rue.speed(15)
rue.penup()
rue.hideturtle()

rue.setheading(225)
rue.forward(300)
rue.setheading(0)
number_of_dots = 100

color_list = [(194, 171, 122), (156, 101, 59),(184, 159, 51), (124, 36, 24), (7, 52, 76), (54, 30, 24),(116, 160, 174), (106, 68, 84), (27, 116, 161),
          (82, 134, 73), (71, 35, 44), (9, 61, 41), (68, 152, 131), (124, 38, 43), (181, 98, 82), (210, 202, 151),
          (116, 160, 174), (106, 68, 84), (27, 116, 161), (82, 134, 73), (71, 35, 44), (9, 61, 41), (68, 152, 131),
          (124, 38, 43), (181, 98, 82), (210, 202, 151),(178, 202, 187), (143, 177, 161), (171, 150, 156),
          (214, 183, 177), (27, 76, 90), (95, 142, 155), (148, 115, 120), (174, 199, 204), (35, 79, 63), (216, 177, 181)]

for dot_count in range (1, number_of_dots+1):
    rue.dot(20, random.choice(color_list))
    rue.forward(50)

    if dot_count % 10 ==0:
        rue.setheading(90)
        rue.forward(50)
        rue.setheading(180)
        rue.forward(500)
        rue.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
