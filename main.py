from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(n=0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)

    snake.move()

    # Detect collision with food - score +1, snake extends
    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.appear()

    # Detect collision with tail - we use list slicing for the list with all segments to ignore the first one (the head)
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 15:
            scoreboard.game_over()
            game_is_on = False

    # Detect collision with walls - if the head goes beyond x and y coords of the borders (300x300) - then game over!
    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280
            or snake.segments[0].ycor() < -280):
        scoreboard.game_over()
        game_is_on = False



screen.mainloop()
