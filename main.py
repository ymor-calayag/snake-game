from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

 # [0, -20, -40]
game_over = False
while not game_over:
    # screen updates every 0.1 second
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food detection
    if snake.head.distance(food) <= 21:
        scoreboard.clear()
        scoreboard.update_score()
        snake.add_snake_segment()
        food.reset()
        food = Food()

    # collision with wall detection
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over = True
        scoreboard.game_over()

    # collision with snake body detection
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()