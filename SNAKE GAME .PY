import turtle
import random
import time


delary= 0.1
sc=0
hc=0
bodies=[]
#credeting a screem
s=turtle.Screen()
s.title("SNAKE GAME")
s.bgcolor("light green")
s.setup(width=600, height= 600)# size of screen 

            
#Creating a head
head= turtle.Turtle()
head.speed(0)
head.shape("square")# which type of shape do you want(snack)
head.color("blue")# shape color of the snack
head.fillcolor("orange")# shape ke ander ka color
head.penup() #no showing line shape
head.ht()# hiding the turtle
head.goto(0,0)# jump to one side to another side
head.st()# showing turtle
head.direction='stop'
 
 
 #Creating  a food for sanke
food= turtle.Turtle()
food.speed(0)
food.shape("circle")# which type of shape do you want(snack)
food.color("orange")# shape color of the snack
food.fillcolor("gray")# shape ke ander ka color
food.penup() #no showing line shape
food.ht()# hiding the turtle
food.goto(150,200)# jump to one side to another side
food.st()# showing turtle


#Creating a  score board
sb= turtle.Turtle()
sb.shape("square")
sb.shape("circle")# which type of shape do you want(snack)
sb.penup() #no showing line shape
sb.ht()# hiding the turtle
sb.goto(-250,250)# jump to one side to another side
sb. write("score:0      |hight score")#score print in the formed of text

# creadting function for movintg in all direction
# Define movement functions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")

# Main game loop
while True:
    s.update()

    # Check for border collisions
    if head.xcor() > 290:
        head.setx(290)
    if head.xcor() < -290:
        head.setx(-290)
    if head.ycor() > 290:
        head.sety(290)
    if head.ycor() < -290:
        head.sety(-290)

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment to the body
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.penup()
        bodies.append(body)

        # Increase the score
        sc += 10
        if sc > hc:
            hs = sc

        # Update the scoreboard
        sb.clear()
        sb.write("Score: {} | High Score: {}".format(sc,hc), align="left", font=("Courier", 14, "normal"))

    # Move the body segments
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check for collision with the body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the body segments
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            # Reset the score
            sc = 0
            delary = 0.1

            # Update the scoreboard
            sb.clear()
            sb.write("Score: {} | High Score: {}".format(sc,hc), align="left", font=("Courier", 14, "normal"))

    time.sleep(delary)

s.mainloop()
# end the game
                        
    
