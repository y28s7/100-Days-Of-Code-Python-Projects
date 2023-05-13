import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()

csv_data = pd.read_csv("50_states.csv")
states = csv_data.state.to_list()

states_guessed_num = 0
states_guessed = []

while states_guessed_num < 50:
    answer_state = screen.textinput(title=f"{states_guessed_num}/50 States Guessed", prompt="Guess a state:").title()

    if answer_state == "Exit":
        break

    if answer_state in states:
        state_data = csv_data[csv_data.state == answer_state]
        states.remove(answer_state)
        states_guessed.append(answer_state)
        writing_turtle.goto(int(state_data.x), int(state_data.y))
        writing_turtle.write(arg=answer_state, move=False, align="left", font=("arial", 8, "normal"))
        states_guessed_num += 1

print("HHHEHEHEHHEJKEKFEFISH")

learn_states = pd.DataFrame(states, columns=["States to Learn"])
learn_states.to_csv("states_to_learn.csv")
