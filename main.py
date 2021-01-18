from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
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

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


## 3.Create another paddle
## 4.Create a ball and move
## 5.Detect collision with wall and bounce
## 6.Detect collision with paddle
## 7.Detect when paddle misses
## 8.Keep score

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

    # detect if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()



print('Pong Game!')
screen.exitonclick()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
