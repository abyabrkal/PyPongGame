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

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


print('Pong Game!')
screen.exitonclick()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
