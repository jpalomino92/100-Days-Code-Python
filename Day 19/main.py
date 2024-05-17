import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Choose a Champion color!: ")
colors = ["blue","orange","purple","red"]
all_turtles = []

y_turtle = -20
for turtle_number in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_number])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_turtle)
    y_turtle += 30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()