import turtle as t
import random as r
import Leaderboard as lb
import winsound

#--global var and objects and game configs
wn = t.Screen()     #everything is clickable
wn.bgcolor('gray9')
wn.setup(600,725)
wn.bgpic('icon.gif')
ruffis = t.Turtle(shape='turtle')
ruffis.shapesize(2)
ruffis.speed(5)
ruffis.color("aquamarine")
timer=20
score=0
clicks=0
ruffisClicks=0
size=1
def MainMenu():
    ruffis.teleport(0,50)
    ruffis.write('Catch A Turtle',align='center',font=("Times New Roman", 50, "bold"))
    ruffis.teleport(0,-80)
    ruffis.write('Space to start',align='center',font=("Times New Roman", 30, "normal"))
    ruffis.teleport(0,0)

def MainGame():
    ruffis.st()
    ruffis.clear()
    
    scoreKeeper = t.Turtle()
    scoreKeeper.speed(0)
    scoreKeeper.teleport(100,315)
    scoreKeeper.color("pink")
    scoreKeeper.ht()

    timeKeeper=t.Turtle()
    timeKeeper.ht()
    timeKeeper.color('goldenrod3')
    timeKeeper.teleport(-200,315)

    accuracyKeeper=t.Turtle()
    accuracyKeeper.ht()
    accuracyKeeper.color('goldenrod3')
    accuracyKeeper.teleport(100,270)

    

    
    interval=1000   
    fontSetup = ("Times New Roman", 30, "normal")
    originalSize=2
    ruffis.shapesize(originalSize)

    #--f(x)m
    #every command that is based on a mouse click MUST HAVE the x,y var passed in
    def ruffisClicked(mouseX,mouseY):    #add any features to this f(x) that trigger when ruffis is sclicked
        global score
        print(f"ruffis was clicked at {mouseX},{mouseY}")
        moveRuffis()
        updateScore()
        shrinkRuffis()
        bgChange()
        updateAccuracy()

    def bgChange():
        wn.bgpic('icon2.gif')
        winsound.Beep(1000,500)
        wn.ontimer(lambda: wn.bgpic("icon.gif"), 500)  #this is from chatGPT

    def shrinkRuffis():
        global clicks
        currentSize = ruffis.shapesize()[0]  # Get current size
        new_size = max(0.5, currentSize - 0.5)  # Decrease size but prevent disappearing
        ruffis.shapesize(new_size)  # Apply new size
        clicks  # Increase click count
        # After 3 shrinks, reset size to original
        if clicks%4 == 0:
            ruffis.shapesize(originalSize)  # Reset size

    def moveRuffis():
        ruffis.stamp()
        newX=r.randint(-290,270)
        newY=r.randint(-290,270)
        ruffis.goto(newX,newY)

    def updateScore():
        global score
        global timer
        score+=1
        timer+=0.5
        print(score)
        scoreKeeper.clear() #clears ANYTHING it wrote
        scoreKeeper.write(f"Score: {score}",font=fontSetup)

    def updateTimer():
        global timer
        timer-=1
        timeKeeper.clear()
        if timer<=0:
            timeKeeper.write(f"Times up",font=fontSetup)
            ruffis.speed(5)
            ruffis.goto(1000,1000)
            manageLeaderBoard()
        else:
            timeKeeper.write(f"Time: {timer}",font=fontSetup)
            timeKeeper.getscreen().ontimer(updateTimer,interval)

    def wnClick(x,y):
        global clicks
        clicks+=1
        updateAccuracy()

    def updateAccuracy():
        global score
        global clicks
        accuracyKeeper.clear()
        if clicks > 0:
            accuracy = (score / clicks) * 100
            accuracyKeeper.write(f"Accuracy: {accuracy:.2f}%", align="center", font=fontSetup) 

    def manageLeaderBoard():    #game over update the hs
        global score
        hsNames = lb.getNames("db.txt")
        hsScores = lb.getScores("db.txt")
        if score > int(hsScores[-1]):
            #should figure out how to get their name w/o the terminal
            currentName = input("Congrats, you made leaderboard!\n\tEnter your name: ")
            lb.updateLeaderboard("db.txt",hsNames,hsScores,currentName,score)
        #lb.drawLeaderboard(False,hsNames,hsScores,scoreKeeper,score)
    ruffis.onclick(ruffisClicked)
    wn.onclick(wnClick)
    wn.ontimer(updateTimer, interval)
        #--events - event handlers



MainMenu()
wn.listen()
wn.onkeypress(MainGame,'space')
#--mainloop
wn.mainloop()
'''
    Features List:
        1. Click a turtle
        2. Turtle move randomly
        3. Score
        4. Timer
        5. High Score rev1 tmr
'''