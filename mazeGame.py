# Fill me in!

background = Rect(0,0,400,400, fill= 'mistyRose')
app.stepsPerSecond = 30
Rect(37,37,323,323)
Rect(0,160,40,80)
Rect(360,160,40,80)

app.movePacman = True

#info 
restartInfo = Label('Use arrow keys / Press "r" to restart' , 200,380,size = 20)

#time 
Label ('Time:', 60,20,size =  20)
time= Label (0,110, 20, size = 20)

#points 
Label('Points:', 320, 20, size= 20)
point =  Label(0,360,20,size = 20)

#pacman 
pacman = Circle(20,200,8,fill= 'lightPink')
pacman.toFront()

# points 
bigStar1 = Star(140,60,13,5,fill ='hotPink')
bigStar2 = Star(140,300,13,5,fill = 'lavenderBlush')
bigStar3 = Star(260,340,13,5,fill= 'deepPink')
bigStar4 = Star (300,180,13,5,fill='red')
bigStar5 = Star (60,340,13,5,fill = 'maroon')
          
littleStar1= Star (100,100,8,5,fill = 'darkViolet')
littleStar2 = Star (340,300,8,5,fill= 'plum')
littleStar3 = Star (180,180,8,5,fill = 'darkTurquoise')
littleStar4 = Star (220,260,8,5,fill = 'aqua')
littleStar5 = Star (340,60,8,5,fill = 'lavender')

# hit property of the points 

bigStar1.hit = False
bigStar2.hit = False
bigStar3.hit = False
bigStar4.hit = False
bigStar5.hit = False

littleStar1.hit = False
littleStar2.hit = False
littleStar3.hit = False
littleStar4.hit = False
littleStar5.hit = False

#maze 
maze = Group(
    Line(40,37,40,160,lineWidth = 6),
    Line(0,240,43,240,lineWidth = 6),
    Line(40,240,40,360,lineWidth = 6),
    Line(0,160,43,160,lineWidth = 6),
 
    Line(120,40,120,80, lineWidth = 6),
    Line(117,80,160,80,lineWidth = 6),
    Line(200,80,280,80,lineWidth = 6), 
    Line(240,80,240,163,lineWidth = 6),
    Line(237,160,160,160,lineWidth = 6),
    Line(160,120,160,163,lineWidth = 6),
    Line(163,120,120,120,lineWidth = 6),
    Line(200,160,200,200,lineWidth = 6),
    Line(203,200,80,200,lineWidth = 6),
    Line(120,203,120,160,lineWidth = 6),
    Line(80,197,80,240,lineWidth = 6),
    Line(77,240,120,240,lineWidth = 6),
    
    Line(360,120,280,120,lineWidth = 6),
    Line(280,117,280,200,lineWidth = 6),
    Line(277,200,320,200,lineWidth = 6),
 
    Line(400,240,200,240,lineWidth = 6),
    Line(400,160,357,160,lineWidth = 6),
    Line(200,237,200,280,lineWidth = 6),
    Line(197,280,240,280,lineWidth = 6),
    
    Line(160,360,160,280,lineWidth = 6),
    Line(163,280,80,280,lineWidth = 6),
    Line(80,277,80,320,lineWidth = 6),
    Line(77,320,120,320,lineWidth = 6),
    
    Line(237,320,320,320,lineWidth = 6),
    Line(320,323,320,280,lineWidth = 6),
    Line(317,280,360,280,lineWidth = 6),
    Line(40,40,363,40,lineWidth = 6),
    Line(360,40,360,160,lineWidth = 6),
    Line(360,240,360,360,lineWidth = 6),
    Line(360,360,40,360,lineWidth = 6),
     )

maze.fill ='white'

#end game 
endGameLose = Group (
    Rect(80,120,240,160,fill = 'mistyRose'),
    Label('Oops!', 200,180,size = 20), 
    Label ('Press r to restart' , 200, 220, size = 20) ) 
    
#timeUp
timeUp = Group (
    Rect(80,120,240,160,fill = 'mistyRose'),
    Label('Time is up !', 200,180,size = 20), 
    Label ('Press r to restart', 200, 220, size = 20))

#you win 
winScreen = Group (
    Rect(80,120,240,160,fill = 'mistyRose'),
    Label('Yayyy !', 200,180,size = 20), 
    Label ('Press r to restart' , 200, 220, size = 20))  
    
endGameLose.visible = False 
timeUp.visible = False 
winScreen.visible = False 

''' press "r" to restart the game''' 

def restartGame():
        
    pacman.centerX = 20
    pacman.centerY = 200
    time.value = 0 
    point.value =  0
    
    app.movePacman = True 
    
    endGameLose.visible = False
    timeUp.visible = False
    winScreen.visible = False 
    
    restartInfo.visible = True 
    
    bigStar1.visible = True 
    bigStar2.visible = True 
    bigStar3.visible = True 
    bigStar4.visible = True 
    bigStar5.visible = True 
    
    littleStar1.visible = True 
    littleStar2.visible = True 
    littleStar3.visible = True 
    littleStar4.visible = True 
    littleStar5.visible = True 
    
    bigStar1.hit = False
    bigStar2.hit = False
    bigStar3.hit = False
    bigStar4.hit = False
    bigStar5.hit = False
    
    littleStar1.hit = False
    littleStar2.hit = False
    littleStar3.hit = False
    littleStar4.hit = False
    littleStar5.hit = False
    
# restart game
def onKeyPress (key): 
    if (key == 'r'):
        restartGame() 
    
#onstep - 
def onStep():
    if (app.movePacman == True):
        time.value += 1 
        youLose() 
        addingPoints()
        youWin()

#wrap around 
    if (pacman.left < 0 ):
        pacman.right = 400
        
    if (pacman.right > 400):
        pacman.left= 0 
        
''' use arrow keys to move pacman'''
#moving pacman 

def onKeyHold (keys):
    
    if (app.movePacman == True):
        if ('right' in keys ):
            pacman.centerX += 4
            
        if ( 'up' in keys ):
            pacman.centerY -= 4
            
        if ( 'left' in keys ):
            pacman.centerX -= 4
            
            
        if (  'down' in keys ):
            pacman.centerY += 4

    #wrap around 

    if (pacman.left < 0 ):
        pacman.right = 400
        
    if (pacman.right > 400):
        pacman.left= 0 
        
''' you lose the game, if you touch the maze or the time goes over 800'''

#you lose
def youLose():
    if (pacman.hitsShape(maze)):
        endGameLose.visible = True
        app.movePacman = False
        restartInfo.visible = False 
        
    elif ((time.value >= 800) and (point.value < 59)):
           timeUp.visible = True 
           app.movePacman = False
           restartInfo.visible = False 
           
def youWin(): 
          
    if  (point.value > 75 ):
         youWin.visible = True 
         app.movePacman = False
         restartInfo.visible = False 

''' the player gets ten (10) points added to their score everytime pacman
    touches any of the big stars'''
    
''' the player gets  five (5) points added to their score everytime pacman 
    touches any of the small stars'''
    
def addingPoints():
    if (bigStar1.hit == False):
        if (pacman.hitsShape(bigStar1)):
            point.value += 10  
            
            bigStar1.visible = False 
            bigStar1.hit = True
    
    if (bigStar2.hit == False):    
        if (pacman.hitsShape(bigStar2)):
            point.value += 10 
            bigStar2.visible = False  
            bigStar2.hit = True 
    
    if (bigStar3.hit == False):    
        if (pacman.hitsShape(bigStar3)):
            point.value += 10 
            bigStar3.visible = False
            bigStar3.hit = True 
    
    if (bigStar4.hit == False):    
        if (pacman.hitsShape(bigStar4)):
            point.value += 10 
            bigStar4.visible = False
            bigStar4.hit = True  
            
    if (bigStar5.hit == False):    
        if (pacman.hitsShape(bigStar5)):
            point.value += 10 
            bigStar5.visible = False
            bigStar5.hit = True
            
    if (littleStar1.hit == False):        
        if (pacman.hitsShape(littleStar1)):
            point.value += 5
            littleStar1.visible = False
            littleStar1.hit = True
    
    if (littleStar2.hit == False):    
        if (pacman.hitsShape(littleStar2)):
            point.value += 5
            littleStar2.visible = False
            littleStar2.hit = True
    
    if (littleStar3.hit == False):    
        if (pacman.hitsShape(littleStar3)):
            point.value += 5
            littleStar3.visible = False
            littleStar3.hit = True
            
    if (littleStar4.hit == False):     
        if (pacman.hitsShape(littleStar4)):
            point.value += 5
            littleStar4.visible = False 
            littleStar4.hit = True

    if (littleStar5.hit == False):     
        if (pacman.hitsShape(littleStar5)):
            point.value += 5
            littleStar5.visible = False 
            littleStar5.hit = True

addingPoints() 

  
app.setMaxShapeCount(5000)