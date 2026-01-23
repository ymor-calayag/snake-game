from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move_distance = 10

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            snake_segments = Turtle("square")
            snake_segments.up()
            snake_segments.color("white")
            snake_segments.goto(x=x_pos, y=0)
            x_pos -= 20
            self.segments.append(snake_segments)
    
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].fd(self.move_distance)
    
    def snake_up(self):
        self.segments[0].setheading(90) # north

    def snake_down(self):
        self.segments[0].setheading(270) # south

    def snake_left(self):
        self.segments[0].setheading(180) # west

    def snake_right(self):
        self.segments[0].setheading(0) # east