
import turtle
import pandas as pd


screen = turtle.Screen()


screen.title("INDIAN STATES GAME")
image = "blank_states.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("states_data.csv")
all_states = data.states.to_list()
guesses = []

while len(guesses) < 27:

    answer_state = screen.textinput(title=f"{len(guesses)}/27  Guess the state",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guesses]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Remaining_states.csv")
        break
        # missing_states = []
        # for state in all_states:
        #     if state not in guesses:
        #         missing_states.append(state)

    if answer_state in all_states:
        guesses.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.ht()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x_cor), int(state_data.y_cor))
        t.write(answer_state)


state_dict = {
    "states": ["Himachal Pradesh", "Punjab", "Rajasthan", "Haryana", "Uttarakhand", "Uttar Pradesh", "Madhya Pradesh",
               "Gujarat", "Maharashtra", "Andhra Pradesh", "Tamil Nadu", "Karnataka", "Goa", "Chhattisgarh",
               "Odisha", "Bihar", "Jharkhand", "West Bengal", "Kerala", "Sikkim", "Arunachal Pradesh", "Mizoram",
               "Tripura", "Meghalaya", "Assam", "Nagaland", "Manipur"],
    "x_cor": [-107, -113, -154, -101, -75, -55, -99, -179, -133, -76, -82, -132, -157, -35, 9, 30, 26, 55, -125, 74,
              160, 144, 121, 108, 133, 169, 161],
    "y_cor": [215, 162, 89, 128, 157, 75, 27, 25, -42, -86, -178, -115, -104, -2, -19, 60, 39, 17, -189, 109, 122, 24,
              42, 65, 89, 84, 62]

}
df = pd.DataFrame(state_dict)
df.to_csv("states_data.csv")


# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
screen.exitonclick()



