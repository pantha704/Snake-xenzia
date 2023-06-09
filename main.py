from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake_alive = True
while snake_alive:
    screen.update()
    time.sleep(0.03)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 10:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.reset()
        snake.reset()

    #detect collision with tail
    for segs in snake.segments[1:]:
        if snake.head.distance(segs) < 5:
            score.reset()
            snake.reset()

screen.exitonclick()
