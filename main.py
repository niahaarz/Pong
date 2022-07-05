from turtle import Screen
from player import Player
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


player1 = Player((-350, 0))
player2 = Player((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")

game_on = True

while game_on:
    time.sleep(ball.currentspeed)
    screen.update()
    ball.move()

    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    
    #Detect collision with paddle
    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() <-320:
        ball.bounce_x()

    
    #Add points to players
    if ball.xcor() > 380:
        ball.resetball()
        score.player1_add_point()


    if ball.xcor() < -380:
        ball.resetball()
        score.player2_add_point()


screen.exitonclick()