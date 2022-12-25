from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1500, height=400)
turtle_colors = ['red', 'green', 'blue', 'yellow', 'brown', 'black', ]
user_bet = screen.textinput('Turtle Race', f'Bet on which turtle(color) is going to win the race.\n{turtle_colors}')
turtle_list = []
x = -230
y = -150
for index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.color(turtle_colors[index])
    new_turtle.setposition(x, y)
    y += 50
    turtle_list.append(new_turtle)

is_game_on = True
while is_game_on:
    for index in range(6):
        turtle_list[index].forward(random.randint(5, 15))
        if turtle_list[index].xcor() >= 730:
            winner_color = turtle_list[index].pencolor()
            is_game_on = False
            if user_bet == winner_color:
                print(f"You won. The winner is {winner_color} turtle.")
            else:
                print(f"You lost. The winner is {winner_color} turtle.")


screen.exitonclick()

