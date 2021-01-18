from turtle import Screen, Turtle

## 1.Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("The Pong Game")
screen.tracer(0)  #no display of animation

## 2.Create and move paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

## 3.Create another paddle
## 4.Create a ball and move
## 5.Detect collision with wall and bounce
## 6.Detect collision with paddle
## 7.Detect when paddle misses
## 8.Keep score

game_is_on = True
while game_is_on:
    screen.update()



print('Pong Game!')
screen.exitonclick()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
