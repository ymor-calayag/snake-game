from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

segments = []

x_pos = 0
for _ in range(3):
    snake_segments = Turtle("square")
    snake_segments.up()
    snake_segments.color("white")
    snake_segments.goto(x=x_pos, y=0)
    x_pos -= 20
    segments.append(snake_segments)

 # [0, -20, -40]
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].fd(10)
    segments[0].lt(90)
        
        

screen.exitonclick()