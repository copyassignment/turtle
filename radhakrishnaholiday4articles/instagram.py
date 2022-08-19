from turtle import * #importing the module

bgcolor('#f3f3f3') #background of the GUI
pencolor('#bc2a8d') #defining the color of the pen
width(23) #defining the thickness of the pen
penup() #start the draw
goto(160,-100) #set the origin for the graphics
pendown() #stop the draw temporarily

left(90) #turn at an angle 
for i in range(4): #loop for 4 times for a square-type shape
    forward(250) 
    circle(34,90) #for border-radius

penup() # for the big circle
goto(85,30) # defining the new origin for the pen
pendown() # stopping the draw
circle(80,360) #built-in function for a circle in the middle

penup() 
goto(110,130) # setting the new origin 
pendown()
circle(7,360) # built-in function for a circle at the top-right

done() # end the program
