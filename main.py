import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)
screen.listen()

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.onkey(snake.snake_up, 'Up')
screen.onkey(snake.snake_down, 'Down')
screen.onkey(snake.snake_left, 'Left')
screen.onkey(snake.snake_right, 'Right')

run = True

while run:

    screen.update()
    time.sleep(0.1)

    snake.snake_forward()

    # detect collision food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.point_up()
        scoreboard.scores()
        snake.extend()

    # detect collision wall
    if snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        run = False
        scoreboard.game_over()

    # detect collision tail
    for segments in snake.turtles[1:]:
        if snake.head.distance(segments) < 10:
            run = False
            scoreboard.game_over()

screen.exitonclick()
