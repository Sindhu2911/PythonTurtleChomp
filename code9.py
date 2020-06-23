# Turtle Graphics Game – Space Turtle Chomp
import turtle
import math
import random
import winsound

turtle.setup(650,650)

# Set up Screen

wn = turtle.Screen()
wn.bgcolor('navy')
wn.bgpic('kbgame-bg.gif')
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.color("white")
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.shapesize(3)
player.penup()
player.speed(0)
score = 0


# Create food
max_foods = 10
foods = []

for count in range(max_foods):
    
    foods.append(turtle.Turtle())
    foods[count].shapesize(1)
    foods[count].color("green")
    foods[count].shape("circle")
    foods[count].penup()
    foods[count].speed(0)
    foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
    
#Set speed variable
speed = 0.1


# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 0.01

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 50:
           return True
       else:
           return False


# Set keyboard binding

turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

while True:
    player.forward(speed)
    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Move food around
        for food in foods:
            food.forward(3)

            # Boundary Food Checking x coordinate
            if food.xcor() > 290 or food.xcor() < -290:
                food.right(180)

            # Boundary Food Checking y coordinate
            if food.ycor() > 290 or food.ycor() < -290:
                food.right(180)

            # Collision checking
            if isCollision(player, food):
                food.setposition(random.randint(-290, 290), random.randint(-290, 290))
                food.right(random.randint(0, 360))
                winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
                score +=1
                # Draw the score on the screen
                mypen.penup()
                mypen.hideturtle()
                mypen.setposition(-290, 310)
                scorestring ="Score: %s" % score
                mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))



