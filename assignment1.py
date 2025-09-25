""" This is your starter code for the Asteroid Kaboom assignment.

You should rename this file and replace this docstring with your own,
as per the documentation standards.

To use this template, make sure that both this file and pixels.py are in the
same folder. From Pyzo, choose Run File as Script.

This template allows you to use a special check_pixel_color function.

For example, check_pixel_color(0, 0, "green") will return 1 if the pixel
at location (0,0) is "green", or 0 if it is not. When you are assigning
points for shots in the assignment, you can multiply the return value by
the number of points for hitting that color.

Sam Scott, McMaster, 2025"""

# Import the turtle module
import turtle
from pixels import check_pixel_color
import random

# Constants (you can change these)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "My First Turtle Program"



# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
screen.tracer(0)

screen.bgcolor("black")
# Create the turtle object
t = turtle.Turtle()

## Start of your code
#t.speed(0)



def stars():
    
    dots_num = 50
    for k in range(dots_num): # make dots
        x_cord = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
        y_cord = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2)
        t.penup()
        t.goto(x_cord,y_cord)
        t.pendown()
        t.dot(3,"white")
    
    t.color("yellow2")
    t.fillcolor("yellow")
    star_amount = 20
    for i in range(star_amount):
        for size in [random.randint(2,9)]:
            x_cord = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
            y_cord = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2) 
            
            t.penup()
            t.goto(x_cord,y_cord)
            t.pendown()
            t.begin_fill()
            
            for j in range(5): 
                t.forward(size)
                t.right(144)
            
            t.end_fill()
        

def asteroids():
    num_sides = random.randint(5,12)
    
    colors = ["grey", "red"]
    for i in range(10):
         
        x_cord = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
        y_cord = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2)
        color = random.choice(colors)
        t.color(color)
        t.fillcolor(color)
        
        t.penup()
        t.goto(x_cord,y_cord)
        t.pendown()
        t.begin_fill()
        for j in range(num_sides):
            for size in [random.randint(10,25)]:
                t.forward(size)
                t.right(360/num_sides)
        t.end_fill()
        t.right(random.randint(1,360)) #orients next asteroid randomnly


stars()
asteroids()




# example of how to use check_pixel_color
#print( check_pixel_color(100, 0, "white") ) # returns 1
#print( check_pixel_color(0, 0, "white") )   # returns 0

## End of your code

# Make a clean exit
screen.exitonclick()
