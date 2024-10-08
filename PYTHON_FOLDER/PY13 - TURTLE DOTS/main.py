# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)# to select rgb colors
tim=t.Turtle()

tim.speed("fastest")
tim.penup()#we dont want the turtle pointer to be shown
tim.setheading(225)#go down towards left so that we can hold the dots correctly on screen
tim.forward(300)#move 50 steps that direction
tim.setheading(0)#again point towrds normal direction
tim.hideturtle()
number_of_dots=100 # 100 dots will be drawn

color_list=[(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for dot_count in range(1,number_of_dots+1): #to have numbers from 1 to 100
    tim.dot(20,random.choice(color_list))# draw a dot
    tim.forward(50)# draw next dot after 50 spaces

    if dot_count%10==0: #after every 10 dots we want the pointer to be back at left side position to draw next 10 dots
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=t.Screen()
screen.exitonclick()
