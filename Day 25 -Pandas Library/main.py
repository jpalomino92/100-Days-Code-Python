import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        state_data = data[data.state == answer_state]
        s.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        s.write(state_data.state.item())

