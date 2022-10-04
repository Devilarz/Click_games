from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Who will win the race ? Enter a color:")
print(user_bet)
colors = ["red", "orange", "green", "blue", "purple", "yellow"]
y_position = [-150, -90, -30, 30, 90, 150]
all_turtles = []

for index_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index_turtle])
    new_turtle.goto(x=-230, y=y_position[index_turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner ! ")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner ! ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()