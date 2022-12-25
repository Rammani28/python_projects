# TODO: 1. Do this then that

# # import turtle
# #
# # timmy = turtle.Turtle()
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
#
# timmy.color('green', 'red')
# my_screen = Screen()
# timmy.forward(255)
# timmy.left(90)
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
# table.add_column('S.N', [1, 2, 3])
table.add_column("A", ["1", "X"])
table.add_column('B', ['X', '0'])
table.add_column("Output", ['1', '0'])
# table.align = 'l'
#TODO: 2.  Now do this todo
print(table)
