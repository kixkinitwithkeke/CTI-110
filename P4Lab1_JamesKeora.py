from turtle import *

#Create the turtle object
timmy = Turtle()
timmy.color("red")

#Draw the square
#Set the pen down
timmy.pendown()
for n in range(4):
    timmy.forward(50)       #move forward 50 spaces
    timmy.left(90)          #turn left 90 degrees
