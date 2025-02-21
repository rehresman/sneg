import turtle
import time
import random
import math

delay = 0.05

score = 0
high_score = 0



# set up screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor(0,0,0)
wn.setup(width=1000, height=1000)
wn.tracer(0) # turns off screen updates

# Background design

design_size = 800
theta = 110
red = 128
green = random.randint(0,255)
blue = 128

design = turtle.Turtle()
design.hideturtle()
turtle.colormode(255)
design.color(red,green,blue)
design.shape("classic")
design.penup()
design.goto(0,-design_size/math.sqrt(2))
design.down()
for steps in range(100):
    design.forward(design_size)
    design.color(red,green,blue)
    design.left(theta)
    design.forward(design_size)
design.showturtle()


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"


# Snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)
food.direction = "stop"

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Score: 0 High Score: 0", align="center", font=("Futura", 24, "normal"))

# Functions


def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def die():
    global score
    time.sleep(2)
    head.goto(0,0)
    head.direction = "stop"

    # Reset the score
    score = 0

    # Hide the segments
    for segment in segments:
        segment.goto(1000,1000)

    # Clear the segments list
    segments.clear()

    pen.clear()
    

    

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# Main game loop
while True:
    wn.update()

    # Check for collision with border
    if head.xcor()>490 or head.xcor()< -490 or head.ycor()>490 or head.ycor()<-490:
        die()

    # Check for food collision
    if head.distance(food) < 20:
        #Move food to random spot
        x = random.randint(-490,490)
        y = random.randint(-490,490)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Futura", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            die()

    time.sleep(delay)







wn.mainloop()
