from turtle import * #importing the module

## setting all the pre-defined values to be used in the program
background_color = '#f3f3f3'
pen_color = '#bc2a8d'
width_val = 23
round_coordA, round_coordB = 34, 90 
circleAx, circleAy = 80, 360
circleBx, circleBy = 7, 360
gotoAx, gotoAy = 85, 30
gotoBx, gotoBy = 160, -100

bgcolor(background_color) #background of the GUI
pencolor(pen_color) #defining the color of the pen
width(width_val) #defining the thickness of the pen
penup() #start the draw
goto(gotoBx, gotoBy) #set the origin for the graphics
pendown() #stop the draw temporarily

left(90) #turn at an angle 
for i in range(4): #loop for 4 times for a square-type shape
    forward(250) 
    circle(round_coordA, round_coordB) #for border-radius

penup() # for the big circle
goto(gotoAx, gotoAy) # defining the new origin for the pen
pendown() # stopping the draw
circle(circleAx, circleAy) #built-in function for a circle in the middle

penup() 
goto(110,130) # setting the new origin 
pendown()
circle(circleBx, circleBy) # built-in function for a circle at the top-right

done() # end the program
