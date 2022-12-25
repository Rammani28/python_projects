import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank-state-us.gif'
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.color('black')
pen.hideturtle()

df = pandas.read_csv('50-states.csv')
state_list = df.state.to_list()

score = 0
game_is_on = True
states_count = len(state_list)
guessed_state = []
while game_is_on:

    answer_state = screen.textinput(f"{score}/{states_count} states correct", "What's the name of another state? ").title().strip()

    if answer_state == "Exit":
        missing_states = [state_name for state_name in state_list if state_name not in guessed_state]
        break

    if answer_state in state_list and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        x = int(df[df.state == answer_state].x)
        y = int(df[df.state == answer_state].y)
        pen.goto(x, y)
        pen.dot()
        pen.write(arg=f"{answer_state}", font=('courier', 12, 'bold'))
        score += 1
        if score == states_count:
            pen.home()
            pen.write("Congratulations! You got them all.")
            break

with open('missed_states.csv', mode='w') as missed_states:
    for state in state_list:
        if state not in guessed_state:
            missed_states.write(f"{state}\n")

print(pandas.read_csv('missed_states.csv', ))
