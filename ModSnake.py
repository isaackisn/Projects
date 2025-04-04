#imports
import turtle as t
import time
import random as r

print("Black moves with WASD")
print("Green moves with arrow keys")
print("Hit p to pause")
print("Hit 1 to play single")
print("Hit 2 to play PVP")



#global var or objects or game configs
delay=0.1
delay2=0.1
bodyParts = []
bodyParts2 = []
paused=False
speed = 20
wn = t.Screen()
wn.bgcolor("ivory4")
wn.setup(width=600,height=600)
wn.title("snake or sum")

head = t.Turtle(shape="triangle")
head.speed(0)
head.penup()
head.direction="stop"   #direction is similar to heading,this controls game play
head2 = t.Turtle(shape="triangle")
head2.speed(0)
head2.penup()
head2.direction="stop"   #direction is similar to heading,this controls game play
head2.color("green4")

food = t.Turtle(shape="turtle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red4")
#f(x)

message = t.Turtle()
message.hideturtle()  # Initially hide the message turtle
message.color("red")
message.penup()
message.goto(0, 0)  # Position the message in the center of the screen

'''
new_color = 0,0,0
def getRColor():
    global new_color
    new_color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))

# Function to change snake color randomly
def change_snake_color():
    global new_color                # Get a random color
    head.color(new_color)  # Apply the new color
'''
# Function to display "Paused" message
def draw_paused_message():
    message.teleport(0,0)
    message.clear()  # Clear any previous message
    message.write("Paused", align="center", font=("Arial", 30, "bold"))
    message.teleport(0,-50)
    message.write("Black moves with WASD", align="center", font=("Arial", 20, "normal"))
    message.teleport(0,-100)
    message.write("Green moves with arrow keys", align="center", font=("Arial", 20, "normal"))    

# Function to clear the paused message
def clear_paused_message():
    message.clear()
    #this f(x) is mainly from GPT, with a couple tweaks
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        draw_paused_message()  # Draw the "Paused" message   (GPT)
    else:
        clear_paused_message()  # Clear the message when unpaused   (GPT)

def move():
        if paused:
            return
        speed=20
        if head.direction == "up":    #"up" is us setting a string value
            head.sety(head.ycor()+speed)  #reset the yval to be up 20 units
        elif head.direction == "down":    
            head.sety(head.ycor()-speed)  #reset the yval to be down 20 units
        elif head.direction == "left":    
            head.setx(head.xcor()-speed)  #reset the xval to be left 20 units
        elif head.direction == "right":   
            head.setx(head.xcor()+speed)  #reset the xval to be right 20 units
def moves():
    if paused:
        return
    if head2.direction == "up":    #"up" is us setting a string value
        head2.sety(head2.ycor()+speed)  #reset the yval to be up 20 units
    elif head2.direction == "down":    
        head2.sety(head2.ycor()-speed)  #reset the yval to be down 20 units
    elif head2.direction == "left":    
        head2.setx(head2.xcor()-speed)  #reset the xval to be left 20 units
    elif head2.direction == "right":   
        head2.setx(head2.xcor()+speed)  #reset the xval to be right 20 units

    
    #pause1.write()
def up():
    if head.direction!="down":
        head.direction="up" 
def ups():
    if head2.direction!="down":
        head2.direction="up"   
#move down
def down():
    if head.direction!="up":
        head.direction="down"
def downs():
    if head2.direction!="up":
        head2.direction="down"
#move left
def left():
    if head.direction!="right":
        head.direction="left"
def lefts():
    if head2.direction!="right":
        head2.direction="left"
#move right
def right():
    if head.direction!="left":
        head.direction="right"
def rights(): 
    if head2.direction!="left":
        head2.direction="right"
#game over
def hideTheBodyParts():
    global bodyParts #Python cheat - where you tell the f(x) that is a global var
    global delay
    global delay2
    head.teleport(0,0)
    head.direction="stop"
    for eachBodyPart in bodyParts:
        eachBodyPart.hideturtle()
    bodyParts=[]
    delay=.1
def hideTheBodyParts2():
    global bodyParts2 #Python cheat - where you tell the f(x) that is a global var
    global delay
    global delay2
    head2.teleport(0,0)
    head2.direction="stop"
    for eachBodyPart in bodyParts2:
        eachBodyPart.hideturtle()
    bodyParts2=[]
    delay2=.1
def snake1snake2(): #when head1 runs into snake body2
   for eachBodyPart in bodyParts2:
        if head.distance(eachBodyPart)<10:
            hideTheBodyParts() 
def snake2snake1(): #when head2 runs into snake body1
    for eachBodyPart in bodyParts:
        if head2.distance(eachBodyPart)<10:
            hideTheBodyParts2()
'''
def pause():
    if pauseGame==False:
        pauseGame=True
    elif pauseGame==True:
        pauseGame=False
   ''' 
#events - event handler - gold/yellow blocks form MIT
#event = when button clicked or when edge reached
#window.onkeypress(command,"keyboard character") - google this some time
#command is a f(x) without calling a function
#   call the up() f(x), you include the ()
#   call the up command, you omit the ()
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.listen()
wn.onkey(toggle_pause, 'p')                 #tells program to listen
wn.listen()
wn.onkey(ups, 'Up')
wn.onkey(downs, 'Down')
wn.onkey(lefts, 'Left')
wn.onkey(rights, 'Right')


#events - event handler - gold/yellow blocks form MIT
#event = when button clicked or when edge reached
#window.onkeypress(command,"keyboard character") - google this some time
#command is a f(x) without calling a function
#   call the up() f(x), you include the ()
#   call the up command, you omit the ()
#tells program to listen


#mainloop for computer
'''
def comp():
    head2.clear()
    head2.ht()
    head.st()
    food.st()
    while True:
        wn.update()
        if abs(head.ycor())>290 or abs(head.xcor())>290:
            head.teleport(0,0)
            head.direction="stop"
            hideTheBodyParts()
        if head.distance(food) < 20:    
            #distance() finds the length between objects
            food.teleport(r.randint(-290,290),r.randint(-290,290))
            bodyPart = t.Turtle(shape='square')
            bodyPart.speed(0)
            bodyPart.penup()
            bodyParts.append(bodyPart)
            delay=delay*.1
        for i in range(len(bodyParts)-1,0,-1):
            newX=bodyParts[i-1].xcor()  #get the x cords of next bodyPart
            newY=bodyParts[i-1].ycor()  #get the y cords of next bodyPart
            bodyParts[i].teleport(newX,newY)

#mainloop for computer PVP
def compPVP():
    head2.clear()
    head.st()
    head2.st()
    food.st()
    while True:
        wn.update()
        if abs(head.ycor())>290 or abs(head.xcor())>290:
            head.teleport(0,0)
            head.direction="stop"
            hideTheBodyParts()
        if head.distance(food) < 20:    
            #distance() finds the length between objects
            food.teleport(r.randint(-290,290),r.randint(-290,290))
            bodyPart = t.Turtle(shape='square')
            bodyPart.speed(0)
            bodyPart.penup()
            bodyParts.append(bodyPart)
            delay=delay*.1
        for i in range(len(bodyParts)-1,0,-1):
            newX=bodyParts[i-1].xcor()  #get the x cords of next bodyPart
            newY=bodyParts[i-1].ycor()  #get the y cords of next bodyPart
            bodyParts[i].teleport(newX,newY)
            
        '''
#mainloop for two player
def PVP():
    global delay
    head2.clear()
    head.st()
    head2.st()
    food.st()
    while True:
        wn.update()             #refreshes the screen
        #check for collision (wall, food, body)
        #   wall collision
        if abs(head.ycor())>290 or abs(head.xcor())>290:
            head.teleport(0,0)
            head.direction="stop"
            hideTheBodyParts()
        if abs(head2.ycor())>290 or abs(head2.xcor())>290:
            head2.teleport(0,0)
            head2.direction="stop"
            hideTheBodyParts2()
                #food collision - distance btwn head and food
        if head.distance(food) < 20:    
            #distance() finds the length between objects
            food.teleport(r.randint(-290,290),r.randint(-290,290))
            bodyPart = t.Turtle(shape='square')
            bodyPart.speed(0)
            bodyPart.penup()
            bodyParts.append(bodyPart)
            delay=.1
            delay*= .2
            delay=max(delay,.001)
            
        if head2.distance(food) < 20:    
            #distance() finds the length between objects
            food.teleport(r.randint(-290,290),r.randint(-290,290))
            bodyPart2 = t.Turtle(shape='square')
            bodyPart2.speed(0)
            bodyPart2.penup()
            bodyParts2.append(bodyPart2)
            delay2=.1
            delay2*= .5
            delay2=max(delay,.001)

        #move the body parts - move the back to the neck
        for i in range(len(bodyParts)-1,0,-1):
            newX=bodyParts[i-1].xcor()  #get the x cords of next bodyPart
            newY=bodyParts[i-1].ycor()  #get the y cords of next bodyPart
            bodyParts[i].teleport(newX,newY)
        for i in range(len(bodyParts2)-1,0,-1):
            newX=bodyParts2[i-1].xcor()  #get the x cords of next bodyPart
            newY=bodyParts2[i-1].ycor()  #get the y cords of next bodyPart
            bodyParts2[i].teleport(newX,newY)

        #move the neck to the head
        if len(bodyParts)>0:
            newX = head.xcor()
            newY = head.ycor()
            neck = bodyParts[0]
            neck.teleport(newX,newY)
        if len(bodyParts2)>0:
            newX = head2.xcor()
            newY = head2.ycor()
            neck2 = bodyParts2[0]
            neck2.teleport(newX,newY)

        snake1snake2()
        snake2snake1()
        move()
        moves()

        #check for body collision
        #if the head is within some distance of another bodyPart
        for eachBodyPart in bodyParts:
            if head.distance(eachBodyPart)<10:
                hideTheBodyParts()
        for eachBodyPart in bodyParts2:
            if head.distance(eachBodyPart)<10:
                hideTheBodyParts2()
        

        time.sleep(delay)
        
#mainloop for single player
def singlePayer():
    global delay
    head2.clear()
    head2.ht()
    head.st()
    food.st()
    while True:
        wn.update()             #refreshes the screen
        #check for collision (wall, food, body)
        #   wall collision
        if abs(head.ycor())>290 or abs(head.xcor())>290:
            head.teleport(0,0)
            head.direction="stop"
            hideTheBodyParts()
                #food collision - distance btwn head and food
        if head.distance(food) < 20:    
            #distance() finds the length between objects
            food.teleport(r.randint(-290,290),r.randint(-290,290))
            bodyPart = t.Turtle(shape='square')
            bodyPart.speed(0)
            bodyPart.penup()
            bodyParts.append(bodyPart)
            delay=.1
            delay*= .5
            delay=max(delay,.001)
            

        #move the body parts - move the back to the neck
        for i in range(len(bodyParts)-1,0,-1):
            newX=bodyParts[i-1].xcor()  #get the x cords of next bodyPart
            newY=bodyParts[i-1].ycor()  #get the y cords of next bodyPart
            bodyParts[i].teleport(newX,newY)

        #move the neck to the head
        if len(bodyParts)>0:
            newX = head.xcor()
            newY = head.ycor()
            neck = bodyParts[0]
            neck.teleport(newX,newY)

        move()


        #check for body collision
        #if the head is within some distance of another bodyPart
        for eachBodyPart in bodyParts:
            if head.distance(eachBodyPart)<10:
                hideTheBodyParts()

        time.sleep(delay)

    #wn.mainloop() - mainloop keeps the window open
def MainMenu():
    head2.teleport(0,0)
    head2.write("Snake", align="center",font=("Arial",100,"bold"))
    head2.teleport(0,-50)
    head2.write("Hit 1 for single", align="center",font=("Arial",50))
    head2.teleport(0,-125)
    head2.write("Hit 2 for PVP", align="center",font=("Arial",50))
    head2.teleport(0,-200)
    head2.write("Hit p to pause", align="center",font=("Arial",50))
    head.ht()
    head2.teleport(0,0)
    head2.ht()
    food.ht()
    wn.onkeypress(singlePayer,"1")
    wn.onkeypress(PVP,"2")
MainMenu()

#wn.onkeypress()
wn.mainloop()