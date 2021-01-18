from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


## 1.Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("The Pong Game")
screen.tracer(0)  #no display of animation

## 2.Create and move paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


print('Pong Game!')
screen.exitonclick()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
