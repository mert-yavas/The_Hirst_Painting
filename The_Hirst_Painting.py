import turtle as t
import random

# settings
t.colormode(255)
t = t.Turtle()
t.shape("turtle")

ordinat = 375
t.teleport(-450, ordinat)
t.speed("fastest")
line = 30
color_list = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132),
              (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239)]

for i in range(26):
    for j in range(30):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(30)
        t.pendown()
        t.dot(20, random.choice(color_list))
    ordinat -= 30
    t.teleport(-450, ordinat)

screen = t.Screen()
screen.exitonclick()
screen.screensize(500, 500)


#pycharmda teleport çalışıyor