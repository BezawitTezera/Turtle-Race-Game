from turtle import Turtle, Screen
from random import randint

is_riding = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet.", prompt="Which color do you want to bet on? ")
colors = ["yellow", "green", "purple", "red","blue"]
all_turtles = []

for i  in range(len(colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230, y = -180 + (i*80))
    all_turtles.append(new_turtle)

if user_bet:
    is_riding = True

while is_riding:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_riding = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you've won. The winner color is {winner_color}.")
            else:
                print(f"you've lost. The winner color is {winner_color}.")

        turtle.forward(randint(0,10))


screen.exitonclick()