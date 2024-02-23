import random
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("#000080")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(15)
tim.speed("fastest")

steps = 0
while steps < 200:
    tim.pencolor(random.choice(colours))
    direction = random.randint(1, 4)
    print(direction)
    match direction:
        case 1:
            tim.forward(40)
        case 2:
            tim.right(40)
        case 3:
            tim.left(40)
        case _:
            tim.backward(40)
    steps += 1












screen = Screen()
screen.exitonclick()