#Todos to tackle this project

#Nr.1 Create the screen
#Nr.2 Create first paddle with functionalities
#Nr.3 Create second one
#Nr.4 Create a ball and make it move
#Nr.5:Detect collision with wall and bounce
#Nr.6 Detect collision with paddle
#Nr.7 Detect when paddle misses
#Nr.8 Keep score



#Nr1
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.setup(height=600, width=800)
my_screen.bgcolor("black")
my_screen.title("Welcome to Pong")
my_screen.tracer(0)


#Nr2: create and move a paddle ---> paddle.py + Nr3: create another paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball=Ball()
score_board=Scoreboard()


my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")

my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")


#Nr4: create ball and make it move-----> ball.py


#Nr7 Detect when paddle misses
#Nr8


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    # Nr5: detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    # Nr6 detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Nr7 Detect when paddle(s) miss:
    #RightPaddle
    if ball.xcor()>380:
        ball.reset_position()
        score_board.l_point()

    #LeftPaddle
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

my_screen.exitonclick()
