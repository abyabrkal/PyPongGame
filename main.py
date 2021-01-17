from turtle import Screen, Turtle

## 1.Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("The Pong Game")
#screen.tracer(0)

## 2.Create and move paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


## 3.Create another paddle
## 4.Create a ball and move
## 5.Detect collision with wall and bounce
## 6.Detect collision with paddle
## 7.Detect when paddle misses
## 8.Keep score


print('Pong Game!')
screen.exitonclick()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
