import turtle
import pandas as pd

PATH_STATES = "50_states.csv"

screen = turtle.Screen()
screen.setup(width=700, height=500)
screen.title("USA Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t =turtle.Turtle()
t.hideturtle()
t.penup()

data = pd.read_csv(PATH_STATES)
states = data.state.to_list()
guessed_states = []


def mark_guessed_state(state, x, y):
    t.goto(x, y)
    t.write(f"{state}")

# # Finding coordinates on screen
# def get_mouse_click_coor(x,y):
#     print(x,y)


# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_states) < len(states):
    answer_state = screen.textinput(title=f"Guessed {len(guessed_states)} out of {len(states)}", prompt="What's another state's name?: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in states and not answer_state in guessed_states:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        # # to get pure value instead of pandas value
        # print(state_row.x.item())
        x = int(state_row.x)
        y = int(state_row.y)
        mark_guessed_state(answer_state, x, y)
