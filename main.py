from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.13)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 16:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -310 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()

    #Detect collision with tell
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
