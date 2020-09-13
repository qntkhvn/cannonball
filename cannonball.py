# Name: Quang Nguyen
# File: cannonball.py
# Desc: A Cannonball Shooting Game Program

from graphics import *
from button import *
from projectile import *
from random import *

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in m/s): "))
    h = 0.0          # Fix initial height at 0.0
    t = 0.01         # Fix time interval at 0.01 sec
    return a, v, h, t

def game():

    # Set the values for the variables
    angle, velocity, h0, time = getInputs()
    
    # Set up graphic window and world coordinate system
    win = GraphWin("Cannonball Shooting Game", 640, 480)
    win.setCoords(-20, -40, 1260, 920)
    win.setBackground("white")

    # Draw axes and labeled ticks
    Line(Point(0,0), Point(1240,0)).draw(win)
    Line(Point(0,0), Point(0,900)).draw(win)

    for x in range (0,1300,100):
        Text(Point(x,-20),str(x)).draw(win)
        Line(Point(x,-10),Point(x,10)).draw(win)
    
    # Set up target
    sx = randrange(800,1200)
    target = Rectangle(Point(sx-10,0),Point(sx+10,100))
    target.setFill("green")
    target.draw(win)
    
    # Display buttons   
    fireButton = Button(win,Point(100,880),160,40,"Fire")
    anglePlusButton = Button(win,Point(100,780),160,40,"Angle +1")
    angleMinusButton = Button(win,Point(100,680),160,40,"Angle -1")
    velocityPlusButton = Button(win,Point(100,630),160,40,"Vel +1")
    velocityMinusButton = Button(win,Point(100,530),160,40,"Vel -1")
    quitButton = Button(win,Point(100,480),160,40,"Quit")

    # Activate buttons
    fireButton.activate()
    anglePlusButton.activate()
    angleMinusButton.activate()
    velocityPlusButton.activate()
    velocityMinusButton.activate()
    quitButton.activate()

    # Display text objects
    shot = 0
    shotText = Text(Point(100,830),"Shots = " + str(shot))
    shotText.draw(win)
    angleText = Text(Point(100,730), str(angle) + " degrees")
    angleText.draw(win)
    velocityText = Text(Point(100,580), str(velocity) + " m/s")
    velocityText.draw(win)
    
    while True:     # Event handlers
        pt = win.getMouse()
        
        if fireButton.clicked(pt):      # Fire button clicked
            
            # Create Projectile object
            cball = Projectile(angle, velocity, h0)
            dot = Circle(Point(0,h0),10)
            dot.setFill("red")
            dot.draw(win)

            # Plot trajectory
            while (cball.getY() >= 0):
                x = cball.getX()
                y = cball.getY()
                Point(x,y).draw(win)
                cball.update(time)
                
            # Move cannonball to final position
            dot.move(x,y)
            dot.setFill("red")

            # Distance between center of target and cannonball
            distance = abs(sx - x)

            # Hit the target and turn it into a pile of rubble
            if (distance <= 10):                              
                target.undraw()
                
                r1 = Rectangle(Point(sx-25,0),Point(sx-5,20))
                r1.setFill("green")
                r1.draw(win)

                r2 = Rectangle(Point(sx-5,0),Point(sx+15,20))
                r2.setFill("green")
                r2.draw(win)

                r3 = Rectangle(Point(sx+15,0),Point(sx+35,20))
                r3.setFill("green")
                r3.draw(win)

                r4 = Rectangle(Point(sx-15,20),Point(sx+5,40))
                r4.setFill("green")
                r4.draw(win)

                r5 = Rectangle(Point(sx+5,20),Point(sx+25,40))
                r5.setFill("green")
                r5.draw(win)

            # Change the shot text object
            shot = shot + 1
            shotText.setText("Shots = " + str(shot))
 
        # Check for changes in angle and velocity
        elif anglePlusButton.clicked(pt):
            angle = angle + 1
        elif angleMinusButton.clicked(pt):
            angle = angle - 1
        elif velocityPlusButton.clicked(pt):
            velocity = velocity + 1
        elif velocityMinusButton.clicked(pt):
            velocity = velocity - 1

        # Check for quit
        elif quitButton.clicked(pt):
            break
            
        # Change the angle and velocity text objects
        angleText.setText(str(angle) + " degrees")
        velocityText.setText(str(velocity) + " m/s")
          
    win.close()     # Close up   
            
game()
