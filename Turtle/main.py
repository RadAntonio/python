# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmader"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)


