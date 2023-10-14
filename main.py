from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)

turtles = []
colors = ["yellow", "red", "black", "green", "blue"]
position = [-200, -100, 0, 100, 200]
for i, c in enumerate(colors):
    new_turtle = Turtle()
    new_turtle.color(c)
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.shapesize(2)
    new_turtle.goto((-360, position[i]))
    turtles.append(new_turtle)

bet = screen.textinput("Select color", "Which gonna win?")
game_is_on = True
winner = ""

result = Turtle()
result.penup()
result.hideturtle()

while game_is_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 360:
            winner = turtle.color()

            if winner == (bet, bet):
                result.color("green")
                result.write("You Win", align="center", font=("Arial", 20, "normal"))
            else:
                result.color("red")
                result.write(f"You Lose, the winner is {winner[0]}", align="center", font=("Arial", 20, "normal"))

            sleep(3)

            result.clear()

            for index, turtle in enumerate(turtles):
                turtle.goto((-360, position[index]))

            bet = screen.textinput("Select color", "Which gonna win?")




screen.exitonclick()
