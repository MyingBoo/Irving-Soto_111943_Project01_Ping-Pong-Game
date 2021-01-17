import turtle as t
import winsound

playerAscore = 0
playerBscore = 0

window = t.Screen()
window.title('Ping Pong Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

#Left Paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape('square')
leftpaddle.color('blue')
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

#Right Paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape('square')
rightpaddle.color('blue')
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#Ball
ball=t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ballxdirection = 0.2
ballydirection = 0.2

#Pen for scoring
pen = t.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font = ('Arial', 24, 'normal'))

#Moving left Paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y = y-90
    leftpaddle.sety(y)

#Moving right Paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y = y-90
    rightpaddle.sety(y)

#Moving Keys
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

#Ball moving
ball.setx(ball.xcor() + ballxdirection)
ball.sety(ball.ycor() + ballydirection)

#main loop
while True:
    window.update()

    #Ball moving
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
        winsound.PlaySound('PongSound.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1
        winsound.PlaySound('PongSound.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0 ,0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(playerAscore, playerBscore), align='center', font = ('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(playerAscore, playerBscore), align='center', font = ('Arial', 24, 'normal'))

    #Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() -40):
        ball.setx(340)
        ballxdirection *= -1
        winsound.PlaySound('PongSound.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() -40):
        ball.setx(-340)
        ballxdirection *= -1
        winsound.PlaySound('PongSound.wav', winsound.SND_ASYNC)

 
      


       
