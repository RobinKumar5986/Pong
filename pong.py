# A simple Python ping pong game created by functions of the Turtle library. Player who gets a score of 7 first wins.

#Date Created : 27/03/2020

import turtle
import os
import random
import math

# Window setup

wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")

# Border and Spikes Drawing

border=turtle.Turtle()
border.hideturtle()
border.penup()
border.color("white")
border.pensize(3)
border.speed(0)
border.setposition(-350,-250)
border.pendown()
border.setheading(90)
for i in range(0,2):
   border.fd(500)
   border.rt(90)
   border.fd(700)
   border.rt(90)
border.rt(90)
border.fd(350)
border.lt(90)
border.fd(500)
border.pensize(0.5)
border.rt(90)
border.fd(350)
for i in range(50):
    border.setheading(210)
    border.fd(10)
    border.setheading(-30)
    border.fd(10)
border.setheading(180)
border.fd(700)
for i in range(50):
    border.setheading(30)
    border.fd(10)
    border.setheading(150)
    border.fd(10)

# Registering Paddles and Ball

turtle.register_shape("block.gif")
p1=turtle.Turtle()
p1.speed(0)
p1.penup()
p1.shape("block.gif")
p1.setposition(-315,0)
p2=turtle.Turtle()
p2.speed(0)
p2.penup()
p2.shape("block.gif")
p2.setposition(315,0)
b=turtle.Turtle()
b.shape("circle")
b.color("yellow")
b.turtlesize(1.5)
b.penup()

# Movement functions and their mapping

def up1():
    y=p1.ycor()
    y=y+30
    if (y>200):
        y=y-30
    p1.sety(y)

def down1():
    y=p1.ycor()
    y=y-30
    if (y<-200):
        y=y+30
    p1.sety(y)

def up2():
    y=p2.ycor()
    y=y+30
    if (y>200):
        y=y-30
    p2.sety(y)

def down2():
    y=p2.ycor()
    y=y-30
    if (y<-200):
        y=y+30
    p2.sety(y)

turtle.listen()
turtle.onkey(up1,'w')
turtle.onkey(down1,'s')
turtle.onkey(up2,'Up')
turtle.onkey(down2,'Down')

# Score Pens and display

s1=0
s2=0
sp1=turtle.Turtle()
sp1.hideturtle()
sp1.speed(0)
sp1.color("white")
sp1.penup()
sp1.setposition(-90,220)
scorestr1="Score : %s" %s1
sp1.write(scorestr1,False,align="left",font=("Arial",14,"normal"))
sp2=turtle.Turtle()
sp2.hideturtle()
sp2.speed(0)
sp2.color("white")
sp2.penup()
sp2.setposition(15,220)
scorestr2="Score : %s" %s2
sp2.write(scorestr2,False,align="left",font=("Arial",14,"normal"))

# Main game loop

b.setheading(random.randint(30,60))
speed=1
while (s1<7 and s2<7):
    b.fd(speed)
    
    # Ball hits a paddle
    
    if (b.ycor()>235 or b.ycor()<-235):
        h=b.heading()
        b.setheading(-1*h)

   # Ball hits spikes
        
    if (b.xcor()>335):
        s1=s1+1
        scorestr1="Score : %s" %s1
        sp1.clear()
        sp1.write(scorestr1,False,align="left",font=("Arial",14,"normal"))
        b.speed(0)
        b.setposition(0,0)
        b.setheading(random.randint(135,225))
        speed=1
    if (b.xcor()<-335):
        s2=s2+1
        scorestr2="Score : %s" %s2
        sp2.clear()
        sp2.write(scorestr2,False,align="left",font=("Arial",14,"normal"))
        b.speed(0)
        b.setposition(0,0)
        b.setheading(random.randint(-45,45))
        speed=1

   # Wall collisions

    if (b.xcor()>290 and (abs(b.ycor()-p2.ycor())<45)):
        b.setx(290)
        h=b.heading()
        b.setheading(180-h)
    if (b.xcor()<-290 and (abs(b.ycor()-p1.ycor())<45)):
        b.setx(-290)
        h=b.heading()
        b.setheading(180-h)

   # Ball acceleration
   
    speed=speed+0.002

# Winner Declaration

b.hideturtle()
w=turtle.Turtle()
w.speed(0)
w.color("white")
w.hideturtle()
if (s1==7):
    w.write("Player 1 wins!",False,align="center",font=("Arial",72,"normal"))
else:
    w.write("Player 2 wins!",False,align="center",font=("Arial",72,"normal"))
wn.exitonclick()
