import turtle

# setup window ==========================
window = turtle.Screen()
window.title("Ping Pong Game By Galia Almejrin")
window.setup(width=1000, height=800)
window.tracer(0)# set delay for update drawings
window.bgcolor(.4,.4,.4)

# setup game objects
#ball
ball=turtle.Turtle()
ball.speed(0) # darwing speed(fastest)
ball.shape("square")
ball.color("pink")
# scale factor * default size (20px * 20px)
ball.shapesize(stretch_len=2, stretch_wid=2)
ball.goto(x=0,y=0)# startvposition
ball.penup()# stop daewing lines when moving
ball_dx, ball_dy = 1 ,1
ball_speed = .4

# center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("pink")
# width => 500px = 25 * 20px default


center_line.shapesize(stretch_len=1,stretch_wid=30)
center_line.penup()
center_line.goto(0,0)

# gamer1
gamer1 = turtle.Turtle()
gamer1.speed(0)
gamer1.shape("square")
gamer1.shapesize(stretch_len=2,stretch_wid=8)
gamer1.color("blue")
gamer1.penup()
gamer1.goto(x=-450,y=0)

# gamer2
gamer2 = turtle.Turtle()
gamer2.speed(0)
gamer2.shape("square")
gamer2.shapesize(stretch_len=2,stretch_wid=8)
gamer2.color("white")
gamer2.penup()
gamer2.goto(x=450,y=0)

# score text
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.goto(x=0,y=310)
score.write("gamer1: 0 gamer2: 0" ,align="center", font=("courier", 14, "normal"))
score.hideturtle() # we hide the object because we only want to see the text
g1_score, g2_score = 0, 0 # variables to hold gamer 1 & gamer 2 score 

 # gamerss movement ===============================
gamerss_speed = 20


def g1_move_up():
    gamer1.sety(gamer1.ycor() + gamerss_speed)


def g1_move_down():
    gamer1.sety(gamer1.ycor() - gamerss_speed)


def g2_move_up():
    gamer2.sety(gamer2.ycor() + gamerss_speed)


def g2_move_down():
    gamer2.sety(gamer2.ycor() - gamerss_speed)

# Get users inputs (kay bindings)
window.listen() # tell the window to expect user inputs
window.onkeypress(g1_move_up,"s") # expect the keyboard in "En" and "small"
window.onkeypress(g1_move_down,"z")
window.onkeypress(g2_move_up,"Up")
window.onkeypress(g2_move_down,"Down")

# game loop ====================
while True:
    window.update()

# ball movement 
    ball.setx(ball.xcor() + ( ball_dx * ball_speed))
    ball.sety(ball.ycor() + ( ball_dy * ball_speed))

    if(ball.ycor() > 290):   #290 => 300(top border) - 10(half ball size)
        ball.sety(290)
        ball_dy *=-1 # invert Y direction

    if(ball.ycor() < -290):   #290 => 300(top border) - 10(half ball size)
        ball.sety(-290)
        ball_dy *=-1 # invert Y direction

    # ball & gamerss collisins ====================
    # collisins with gamers 1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (gamer1.ycor()-60)and ball.ycor() < (gamer1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

        # collisins with gamers 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (gamer2.ycor()-60)and ball.ycor() < (gamer2.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

        # score handling
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1 # invert X direction 
        score.clear()
        g1_score += 1
        score.write(f"gamer1: {g1_score} gamer2: {g2_score}" ,align="center", font=("courier", 14, "normal"))

              # score handling
    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1 # invert X direction
        score.clear()
        g2_score += 1
        score.write(f"gamer1: {g1_score} gamer2: {g2_score}" ,align="center", font=("courier", 14, "normal")) 
