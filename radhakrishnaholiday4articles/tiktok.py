from turtle import * #importing the module

width(20) # width of the pen
bgcolor('black') #background of the GUI
rangharu= ['#db0f3c', '#50ebe7','white'] #all colors stored in a list 
thaau = [(0,0), (-5,13), (-5,5)] # all coordinates stored in a list of tuples
for (x,y),col in zip(thaau,rangharu): # loop through the colors and tuples at the same time
    up() 
    goto(x,y) # move the pen according to the current tuple in the loop 
    down()
    color(col) # set the new color 
    left(180) # start drawing  
    circle(50, 270) # built-in function to draw a circle
    forward(120)
    left(180) 
    circle(50, 90) # built-in function to draw a circle
done() # end of the program