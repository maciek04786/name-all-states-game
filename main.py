import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    screen.title(f"{len(guessed_states)}/50 States Correct")
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if states_data.state.str.contains(answer_state).any():
        answer_x = float(states_data[states_data.state == answer_state]["x"])
        answer_y = float(states_data[states_data.state == answer_state]["y"])
        writer.goto(answer_x, answer_y)
        writer.write(answer_state)
        guessed_states.append(answer_state)

remaining_states = [state for state in all_states if state not in guessed_states]

data = pandas.DataFrame(remaining_states)
df = data.to_csv("remaining_states.csv")
