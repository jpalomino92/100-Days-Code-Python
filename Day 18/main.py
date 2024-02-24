import random
import turtle as t

t.colormode(255)
pepito = t.Turtle()
pepito.speed("fastest")
pepito.penup()
pepito.hideturtle()
rgb_colors = [(177, 59, 36), (239, 224, 2), (2, 99, 76), (215, 63, 123), (130, 36, 20), (245, 231, 46), (94, 171, 225), (237, 161, 192), (179, 56, 111), (225, 72, 52)]

pepito.setheading(225)
pepito.forward(300)
pepito.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1 ):
    pepito.dot(20, random.choice(rgb_colors))
    pepito.forward(50)

    if dot_count % 10 == 0 :
        pepito.setheading(90)
        pepito.forward(50)
        pepito.setheading(180)
        pepito.forward(500)
        pepito.setheading(0)





screen = t.Screen()
screen.exitonclick()