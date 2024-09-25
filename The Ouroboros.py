#Snake Game - Maria Yagual
#importing libraries
import turtle
import random
import time
import pygame

#default game settings
delay = 0.1
levelS = 1
score = 0
highScore = 0

#Color Options
color1 = "black"
color2 = "white"
color3 = "green"
color4 = "honeydew"
color5 = "thistle"
color6 = "red"
color7 = "gold"
color8 = "maroon"
color9 = "blue"
color10 = "grey"
color11 = "dark red"
color12 = "yellow"
color13 = "midnightblue"

#Screen Size
sizeWx = 920 #x-axis
sizeWy = 780 #x-axis

#Window Setup
displayR = turtle.Screen()
displayR. title("THE OUROBOROS ( ⚆ _ ⚆ )")
displayR.bgcolor(color4)
displayR.setup(sizeWx,sizeWy)
displayR.tracer(0)

#Window Input for username to later display in the welcoming statement
displayR2 = turtle.Screen()
displayR2.setup(sizeWx,sizeWy)
userName = turtle.textinput("User Name Screen", "Enter your username: ") #Creates the input function

#Welcoming statement with username
pen1 = turtle.Turtle()
pen1.up()
pen1.goto(0, 375) #position
pen1.write(("Welcome " + userName + "! The rules are simple, the snake must"), align=("center"), font=("Courier", 20, "normal"))
pen1.goto(0, 355) #position
pen1.write("eat the apples and pears to grow. Since this is an ouroboros ", align=("center"), font=("Courier", 20, "normal"))
pen1.goto(0, 335) #position
pen1.write("snake, you have 3 chances before your body length restarts. ", align=("center"), font=("Courier", 20, "normal"))
pen1.hideturtle()

#High score - speed statement
pen1 = turtle.Turtle()
pen1.up()
pen1.goto(0, -340) #position
pen1.write(("Reach highest speed at level 44 with a score of 220"), align=("center"), font=("Courier", 20, "normal"))
pen1.goto(0, -360) #position
pen1.write(("Accept the challenge?"), align=("center"), font=("Courier", 20, "normal"))
pen1.hideturtle()


#GRID AND BORDER SETTINGS
#Functions for border
borderS1= turtle.Screen()
borderS = turtle.Turtle()
# Setting size
borderS1.setup(800,800) #set size of border
# set turtle features
borderS.speed(100)
borderS.left(90)
borderS.color(color6)
# Border
borderS.penup()
borderS.forward(310)#up
borderS.pendown()
borderS.right(90)
borderS.forward(310)
borderS.right(90)
borderS.forward(620)#side 3
borderS.right(90)
borderS.forward(620)
borderS.right(90)
borderS.forward(620)
borderS.right(90)
borderS.forward(310)
borderS.penup()
borderS.hideturtle()

# Functions for grid
gridS1 = turtle.Screen()
gridS = turtle.Turtle()
# Setting size
gridS1.setup(800,800)
# set turtle features
gridS.speed(100)
gridS.left(90)
gridS.color(color13)
# Grid
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(10)
gridS.pendown()
gridS.right(90)
gridS.forward(310)#y-axis
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20) #square pixel size
gridS.right(90)
#Line
gridS.pendown()
gridS.forward(620)#y-axis
gridS.penup()
gridS.right(90)
gridS.forward(20) #square pixel size
gridS.right(90)
#Beginning of x-axis lines
#Line 1 x-axis
gridS.pendown()
gridS.forward(300)
gridS.right(90)
gridS.forward(320)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20) #square pixel size
gridS.left(90)
#Line 2 x - axis
gridS.pendown()
gridS.forward(620)#x-axis
gridS.penup()
gridS.left(90)
gridS.forward(20) #square pixel size
gridS.left(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 3 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Line 4 x-axis
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 5 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 6 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 7 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 8 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 9 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
gridS.pendown()
gridS.forward(620)#x-axis
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 10 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(320)
gridS.penup()
gridS.left(90)
#Line 11 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 12 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 13 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 14 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 15 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 16 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 17 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 18 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 19 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 20 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 21 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 22 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 21 x - axis
gridS.pendown()
gridS.forward(620)
#Direction
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 22 x - axis
gridS.pendown()
gridS.forward(620)
gridS.penup()
#Starting y - axis lines
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 1 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 2 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 3 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 4 y-axis
gridS.pendown()
gridS.forward(620)
##
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 5 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 6 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 7 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 8 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 9 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 10 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 11 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 12 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 13 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 14 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 15 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 16 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 17 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 18 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 19 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 20 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 21 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 22 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 23 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 24 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 25 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 26 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 27 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 28 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 2
gridS.penup()
gridS.left(90)
gridS.forward(20)#square pixel size
gridS.left(90)
#Line 29 y-axis
gridS.pendown()
gridS.forward(620)
#Direction 1
gridS.penup()
gridS.right(90)
gridS.forward(20)#square pixel size
gridS.right(90)
#Line 30 y-axis
gridS.pendown()
gridS.forward(620)
gridS.hideturtle()

#Sprite 1 - Snake
snakeSprite = turtle.Turtle()
snakeSprite.speed(0)
snakeSprite.shape("square")
snakeSprite.color(color3)
snakeSprite.penup()
snakeSprite.goto(0,0)
snakeSprite.direction = "stop"

#Additional Sprites - Apple and Pear
sSprite = turtle.Turtle()
sSpritesA = random.choice(["triangle","circle"]) #options
colors = random.choice([color6,color7,color8])
sSprite.speed(0)
sSprite.shape(sSpritesA)
sSprite.color(colors)
sSprite.penup()
sSprite.goto(0,0)

#Text to display current player's score and to display highest score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color(color11)
pen.penup()
pen.hideturtle()
pen.goto(0, 310) #position
pen.write("Score:0 High score:0", align = "center" , font=("Courier", 20, "bold")) #Score Counter


# assigning key directions using coordinates
def group():
    if snakeSprite.direction != "down":
        snakeSprite.direction = "up"

def godown():
    if snakeSprite.direction != "up":
        snakeSprite.direction = "down"

def goleft():
    if snakeSprite.direction != "right":
        snakeSprite.direction = "left"

def goright():
    if snakeSprite.direction != "left":
        snakeSprite.direction = "right"

def move():
    if snakeSprite.direction == "up":
        y = snakeSprite.ycor()
        snakeSprite.sety(y + 20)
    if snakeSprite.direction == "down":
        y = snakeSprite.ycor()
        snakeSprite.sety(y - 20)
    if snakeSprite.direction == "left":
        x = snakeSprite.xcor()
        snakeSprite.setx(x - 20)
    if snakeSprite.direction == "right":
        x = snakeSprite.xcor()
        snakeSprite.setx(x + 20)

#Assinging key directions to display
displayR.listen()
displayR.onkeypress(group, "Up") #Arrow up
displayR.onkeypress(godown, "Down") #Arrow down
displayR.onkeypress(goleft, "Left") #Arrow left
displayR.onkeypress(goright, "Right") #Arrow right


# Main Gameplay
parts = [] # To later add on to the snake's body

#Background Sound
from pygame import mixer

sound1 = 'BackgroundMusic.ogg'
mixer.init()
mixer.music.load(sound1)
mixer.music.play()


#Loop for inner box using coordinates/pixels
while True:
    displayR.update()
    position1 = snakeSprite.xcor()
    position2 = snakeSprite.ycor()
    if position1 > 290:
        time.sleep(1)
        snakeSprite.goto(0, 0)
        snakeSprite.direction = "Stop"
        colors = random.choice([color6, color9,color3])
        shapes = random.choice(["square", "circle"])
        #Crash Sound
        sound2 = 'SadSound2.ogg'
        mixer.init()
        mixer.music.load(sound2)
        mixer.music.play()
        mixer.music.queue(sound1)

        """
        spark = turtle.Turtle()
        spark.update(position2)

        spark.pensize(.5)
        spark.speed(400)
        spark.left(90)

        # sparks
        spark.color("orange")
        for step in range(40):
            spark.forward(20)
            spark.left(180)
            spark.forward(20)
            spark.left(9)
        spark.hideturtle()
        """

    elif position1 < -290:
        time.sleep(1)
        snakeSprite.goto(0, 0)
        snakeSprite.direction = "Stop"
        colors = random.choice([color6, color9, color3])
        shapes = random.choice(["square", "circle"])
        #Crash Sound
        sound2 = 'SadSound2.ogg'
        mixer.init()
        mixer.music.load(sound2)
        mixer.music.play()
        mixer.music.queue(sound1)
        """
        spark = turtle.Turtle()
        spark.update(position1)

        spark.pensize(.5)
        spark.speed(400)
        spark.left(90)

        # sparks
        spark.color("orange")
        for step in range(40):
            spark.forward(20)
            spark.left(180)
            spark.forward(20)
            spark.left(9)
        spark.hideturtle()
        """

    elif position2 > 290:
        time.sleep(1)
        snakeSprite.goto(0, 0)
        snakeSprite.direction = "Stop"
        colors = random.choice([color6, color9, color3])
        shapes = random.choice(["square', 'circle"])
        # Crash Sound
        sound2 = 'SadSound2.ogg'
        mixer.init()
        mixer.music.load(sound2)
        mixer.music.play()
        mixer.music.queue(sound1)

        """
        spark = turtle.Turtle()
        spark.update(position2)

        spark.pensize(.5)
        spark.speed(400)
        spark.left(90)

        # sparks
        spark.color("orange")
        for step in range(40):
            spark.forward(20)
            spark.left(180)
            spark.forward(20)
            spark.left(9)
        spark.hideturtle()
        """

    elif position2 < -290:
        time.sleep(1)
        snakeSprite.goto(0, 0)
        snakeSprite.direction = "Stop"
        colors = random.choice([color6, color9, color3])
        shapes = random.choice(["square", "circle"])
        #Crash Sound
        sound2 = 'SadSound2.ogg'
        mixer.init()
        mixer.music.load(sound2)
        mixer.music.play()
        mixer.music.queue(sound1)
        """
        spark = turtle.Turtle()
        spark.update(position2)

        spark.pensize(.5)
        spark.speed(400)
        spark.left(90)

        # sparks
        spark.color("orange")
        for step in range(40):
            spark.forward(20)
            spark.left(180)
            spark.forward(20)
            spark.left(9)
        spark.hideturtle()

        """

        for body in parts:
            body.goto(1000, 1000)
        parts.clear()
        score = 0 #restarts score
        delay = 0.1
        levelS = 1
        pen.clear()
        pen.write("Score: {} High score: {}".format(
            score, highScore), align="center", font=("Courier", 20, "bold"))
        #Restarts background music when player hits wall
        sound1 = 'BackgroundMusic.ogg'
        mixer.init()
        mixer.music.load(sound1)
        mixer.music.play()

    if snakeSprite.distance(sSprite) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        sSprite.goto(x, y)

        # Adding segments together
        bodyPart = turtle.Turtle()
        bodyPart.speed(0)
        bodyPart.shape("square")
        bodyPart.color(color3)  # tail color
        bodyPart.penup()
        parts.append(bodyPart)
        delay -= 0.001
        score += 1
        #formating to add up to the high score and current score while user playing
        if score > highScore:
            highScore = score

        pen.clear()
        pen.write("Score: {} High score: {}".format(
            score, highScore), align="center", font=("Courier", 20, "bold"))
        sound3 = 'AppleSound.ogg'
        mixer.init()
        mixer.music.load(sound3)
        mixer.music.play()
        mixer.music.queue(sound1)

    # Checking for head collisions with body segments
    for index in range(len(parts) - 1, 0, -1):
        x = parts[index - 1].xcor()
        y = parts[index - 1].ycor()
        parts[index].goto(x, y)

    if len(parts) > 0:
        x = snakeSprite.xcor()
        y = snakeSprite.ycor()
        parts[0].goto(x, y)

#Positioning Additonal sprites - apple/pear
    move()
    for apple in parts:
        if apple.distance(snakeSprite) < 20:
            time.sleep(1)
            snakeSprite.goto(0, 0)
            snakeSprite.direction = "stop"
            colors = random.choice([color6, color9, color3]) #colors for pear/apple
            shapes = random.choice(["circle", "triangle"]) #pear/apple


            for apple in parts:
                apple.goto(1000, 1000)
            apple.clear()
            score = 0
            delay = 0.1
            levelS = 1
            pen.clear()
            pen.write("Score: {} High score: {}".format(
                score, highScore), align="center", font=("Courier", 20, "bold")) #Formats scores whenever user scores


#Creating Levels based on speed and score. Up to 44 levels - delay function creates the speed for snake movement
    #Reach highest speed at level 44 with a score of 210
    #Add sound to level up
    if levelS == 1 and score == 5:
        levelS +=1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold")) #Updates Level number

        #Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1) #continues background music

    elif levelS == 2 and score == 10:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 3 and score == 15:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 4 and score == 20:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 5 and score == 25:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 6 and score == 30:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 7 and score == 35:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 8 and score == 40:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 9 and score == 45:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 10 and score == 50:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 11 and score == 55:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 12 and score == 60:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 13 and score == 65:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))#Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 14 and score == 70:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 15 and score == 75:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 16 and score == 80:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 17 and score == 85:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 18 and score == 90:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 19 and score == 95:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 20 and score == 100:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 21 and score == 105:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 22 and score == 110:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 23 and score == 115:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 24 and score == 120:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 25 and score == 125:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 26 and score == 130:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 27 and score == 135:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 28 and score == 140:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 29 and score == 145:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 30 and score == 150:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music#continues background music

    elif levelS == 31 and score == 155:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 32 and score == 160:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 33 and score == 165:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 34 and score == 170:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 35 and score == 175:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 36 and score == 180:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 37 and score == 185:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 38 and score == 190:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 39 and score == 195:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 40 and score == 200:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)


    elif levelS == 41 and score == 205:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 42 and score == 210:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 43 and score == 215:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    elif levelS == 44 and score == 220:
        levelS += 1
        delay *= 0.9
        pen.clear()
        pen.write("Level:{}".format(levelS), align="right", font=("Courier", 20, "bold"))# Updates Level number

        # Play when user levels up
        sound5 = 'LevelUp.ogg'
        mixer.init()
        mixer.music.load(sound5)
        mixer.music.play()
        mixer.music.queue(sound1)#continues background music

    time.sleep(delay)

displayR.exitonclick() #needed to have display continuously
