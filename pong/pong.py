import turtle
import time

wn = turtle.Screen()
wn.title("Pong by marim")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

game_paused = False

ball_speeds = {"Basic": 1, "Medium": 1.5, "Hard": 2.5}
current_difficulty = "Basic"

selection_boxes = {}

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

#Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"normal"))

#Fonksiyon
def pause_game():
    global game_paused
    game_paused = not game_paused

def set_ball_speed(difficulty):
    global current_difficulty
    current_difficulty = difficulty
    ball.dx = ball_speeds[difficulty]
    ball.dy = -ball_speeds[difficulty]
    update_selection_boxes(difficulty)

def set_difficulty_basic():
    set_ball_speed("Basic")

def set_difficulty_medium():
    set_ball_speed("Medium")

def set_difficulty_hard():
    set_ball_speed("Hard")

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def update_selection_boxes(selected_difficulty):
    for difficulty, box in selection_boxes.items():
        if difficulty == selected_difficulty:
            box.hideturtle()
        else:
            box.showturtle()

for i, (difficulty, speed) in enumerate(ball_speeds.items(), start=1):
    selection_boxes = turtle.Turtle()
    selection_boxes.speed(0)
    selection_boxes.shape("square")
    selection_boxes.color("black")
    selection_boxes.shapesize(stretch_wid=2,stretch_len=8)
    selection_boxes.penup()
    selection_boxes.goto(0, 100 - i * 30)
    selection_boxes.hideturtle()
    selection_boxes[difficulty] = selection_boxes

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(pause_game, "p")
wn.onkeypress(set_difficulty_basic,"1")
wn.onkeypress(set_difficulty_medium,"2")
wn.onkeypress(set_difficulty_hard,"3")

delay = 0.01
# Oyun döngüsü
while True:
    wn.update()

    if game_paused:
        time.sleep(0.1)
        continue

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    #Paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue") 
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1


    time.sleep(delay)