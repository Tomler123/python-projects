from turtle import Screen, Turtle
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
delay = 0.1

while(game_is_on):
    time.sleep(delay)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle()
        delay *= 0.85

    if ball.xcor() > 360:
        time.sleep(0.3)
        ball.reset_position()
        scoreboard.r_point()
        delay = 0.1

    if ball.xcor() < -360:
        time.sleep(0.3)
        ball.reset_position()
        scoreboard.l_point()
        delay = 0.1

screen.exitonclick()