# Snake Game

This project recreates the traditional Snake game in a graphical window using Turtle. The snake moves continuously, responds to keyboard input, grows when it eats food, and ends the game when a collision occurs. The score increases each time food is collected.

**Technologies Used**

+ ```Python```
+ ```turtle``` module for graphics and animation
+ ```time``` module for game timing
+ Object-Oriented Programming (OOP)

**Features**

+ Real-time snake movement with smooth animation
+ Keyboard controls (arrow keys)
+ Random food spawning
+ Snake growth on food collision
+ Score tracking
+ Game-over detection for wall and self-collisions

**What Users Can Do**

+ Control the snake using the arrow keys
+ Eat food to increase the snake’s length
+ Track their score as the game progresses
+ Lose the game by hitting the wall or the snake’s body

**The Process / How It’s Built**

+ The game window is created using the ```Turtle``` ```Screen```.
+ The snake is implemented as a list of ```Turtle``` segments managed by a ```Snake``` class.
+ Food is represented as a ```Turtle``` object that spawns at random locations.
+ A scoreboard displays the player’s score and the game-over message.
+ The game loop updates the screen, moves the snake, and checks for collisions each frame.
