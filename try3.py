from os import TMP_MAX
from tkinter import *
from tkinter import font
import random
from types import BuiltinFunctionType
import winsound
import os
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x700")
root.resizable(False,False)
root.title("Project Game")
canvas = Canvas(root, width=800, height=700)
# =====================image and background=====================
bgStart = ImageTk.PhotoImage(Image.open("image/bg-start.png"))
bgHelp = ImageTk.PhotoImage(Image.open("image/Rule.png"))
bgPlay = ImageTk.PhotoImage(Image.open("image/bg_play.png"))
enemyIamge= ImageTk.PhotoImage(Image.open("image/plane-match.png"))
playerImage = ImageTk.PhotoImage(Image.open("image/plane-player (4).png"))
playerBullet = ImageTk.PhotoImage(Image.open("image/playerBullet 1 (1).png"))
lostBg = ImageTk.PhotoImage(Image.open("image/lost.png"))
winBg = ImageTk.PhotoImage(Image.open("image/win-game.png"))

# =====================variable=====================
gameProcessing = True
score = 0
gameWin = False
lifeOfPlayer = 5
displayHomeBg = True
displayPlayBg = False
listBulletOfPlayer = []
listOfEnemy  = []
listBulletOfEnemy = []
moveEnemys = 0
playerX = 310
playerY = 500
paused = False
positionXBullet = 0
positionYBullet = 0
# =====================sound=====================
def displaySound():
    winsound.PlaySound('sound\drop.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.after(2000,displaySound)
# =====================Start Window=====================
def displayBackground():
    global displayHomeBg, displayPlayBg, score
    canvas.delete("all")
    if displayHomeBg:
        canvas.create_image(0,0, anchor=NW, image = bgStart)
        # ===========start===========
        canvas.create_rectangle(300,280,500,330, fill="#09b31d", tags="start", outline="")
        canvas.create_text(400,305, text="Start" ,font=('VNI-Bodon-Poster','25','bold'), fill="white",tags="start")
        # ===========Exit===========
        canvas.create_rectangle(300,350,500,400, fill="white", tags="exit", outline="")
        canvas.create_text(400,375, text="Exit" ,font=('VNI-Bodon-Poster','25','bold'),tags='exit')
        # ===========Help===========
        canvas.create_rectangle(300,420,500,470, fill="white", tags="help", outline="")
        canvas.create_text(400,444, text="Help" ,font=('VNI-Bodon-Poster','25','bold'),tags='help')
        winsound.PlaySound('sound\start-game.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif displayPlayBg:
        canvas.delete("all")
        canvas.create_image(0,0, anchor=NW, image = bgPlay)
        canvas.create_text(700,685,text='Score: 00'+str(score),font=('Roboto','22','bold'),fill='white',tags="myScore")
        playGame()
        blood()
        
#=====================back to window=====================
def goBack(event):
    global displayHomeBg
    displayHomeBg = True        
    displayBackground()   
# ===================== Display help player to paly this game =====================
def exitFromGame(event):    
    root.destroy()
displayBackground()
# =====================display rule=====================
def gameRule():
    canvas.delete("all")
    canvas.create_image(0,0, anchor=NW, image = bgHelp)
# =====================click help=====================
def displayHelp(event):
    global displayHomeBg
    displayHomeBg = False
    displayBackground()
# =====================Create  text help=====================
def createHelp():
    canvas.delete('Exit')
    canvas.delete('Start')
# =====================display new window after click start=====================
def windowPlay(event):
    global displayPlayBg, displayHomeBg,score
    displayPlayBg = True
    displayHomeBg = False
    displayBackground()
def playGame():
    global score
    createPlayer()
    moveBullet()
    createEnemy()
    moveEnemy()
    root.bind('<s>',moveRight)
    root.bind('<a>',moveLeft)
    root.bind('<w>',moveUp)
    root.bind('<d>',moveDown)
    root.bind('<space>',createBullet) 

def bulletMeetEnemy():
    global score,displayPlayBg, gameProcessing,gameWin
    if not gameWin:
        meetEn = isMeetEnemy(listBulletOfPlayer,listOfEnemy)
        if len(meetEn) > 0:
            listBulletOfPlayer.remove(meetEn[0])
            listOfEnemy.remove(meetEn[1])
            canvas.delete(meetEn[0])
            canvas.delete(meetEn[1])
            score +=1 
            if score >3:
                gameProcessing = False
                gameWin = True
        scoreOfPlayer()

def scoreOfPlayer():
    global score
    canvas.delete("myScore")
    canvas.create_text(700,685,text='Score: 00'+str(score),font=('Roboto','22','bold'),fill='white',tags="myScore")

# Game Lost and Win
def finishGame():
    global gameWin
    canvas.delete("all")
    if gameWin:
        canvas.create_image(0,0, anchor=NW, image = winBg)
    else:
        canvas.create_image(0,0, anchor=NW, image = lostBg)
        canvas.create_rectangle(90,90,300,300,fill="blue",tags="next")
        
    
# To Restart
def restart(event):
    root.destroy()
    os.system('Project-game.py')
canvas.tag_bind("next","<Button-1>", windowPlay)

# =====================create enemies=====================
# create enemy==================================

def createEnemy():
    global enemy, gameProcessing
    if len(listOfEnemy)<5:
        enemy = canvas.create_image(random.randrange(20,650),-10,anchor = NW,image=enemyIamge)
        listOfEnemy.append(enemy)
    if gameProcessing:
        canvas.after(2000,createEnemy)
    else:
        finishGame()
# =====================move enemy=====================  

def moveEnemy():
    global listOfEnemy, positionXBullet,playerX,playerY, lifeOfPlayer, score ,gameProcessing
    for enemies in listOfEnemy:
        canvas.move(enemies,0,12)
        position  = canvas.coords(enemies)
        if position[1] > 600  :
            listOfEnemy.remove(enemies)
            canvas.delete(enemies)
            lifeOfPlayer -= 1
        elif ((playerY-position[1] >= -100 and playerY-position[1] <= 10) and (playerX-position[0]>=-80 and playerX-position[0]<=50)):
            listOfEnemy.remove(enemies)
            canvas.delete(enemies)
            lifeOfPlayer -= 1
        blood()   
        if lifeOfPlayer == 0:
            gameProcessing = False
    if gameProcessing:
        canvas.after(150,moveEnemy)
    else:
        finishGame()
# =====================create player=====================
def createPlayer():
    global player, playerX, playerY
    player = canvas.create_image(playerX,playerY,anchor = NW, image= playerImage)
#  =====================create bullet of player=====================
def createBullet(event):
    global playerX, playerY,bulletOfPlayer,listBulletOfPlayer,bulletOfPlayer,gameProcessing
    if gameProcessing:
        bulletOfPlayer = canvas.create_image(playerX+48,playerY, image=playerBullet,tags= 'player-bullet')
        listBulletOfPlayer.append(bulletOfPlayer)
        winsound.PlaySound('sound\shoot.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
#     =====================move bullet of player=====================
def moveBullet():
    global bulletOfPlayer,listBulletOfPlayer, gameWin
    if not gameWin:
        for bulletOfPlayer in listBulletOfPlayer:
            canvas.move(bulletOfPlayer,0,-20)
            position  = canvas.coords(bulletOfPlayer)
            if position[1] <20 :          
                listBulletOfPlayer.remove(bulletOfPlayer)
                canvas.delete(bulletOfPlayer)
        bulletMeetEnemy()
        canvas.after(50,moveBullet) 

# ==============================is bullet of player meet enemy==============================
def isMeetEnemy(listBulletOfPlayer,listOfEnemy):
    delete = []
    for playerBullet in listBulletOfPlayer:
        positionBulletOfPlayer = canvas.coords(playerBullet)
        for enemy in listOfEnemy:
            positionOfEnemy = canvas.coords(enemy)           
            if ((positionBulletOfPlayer[1]- positionOfEnemy[1]<=10) and (positionBulletOfPlayer[1]- positionOfEnemy[1]>= -10)) and (((positionBulletOfPlayer[0] - positionOfEnemy[0]>=0) and (positionBulletOfPlayer[0] - positionOfEnemy[0]<=60))):
                delete.append(playerBullet)
                delete.append(enemy)
    return delete

# ==============================Move player ==============================
    # =====================moveRight=====================
def moveRight(event):
    global playerX,paused,playerY
    paused = False
    if playerX < 670:
        playerX +=20 
    canvas.moveto(player,playerX,playerY)
    # =====================moveLeft===================== 
def moveLeft(event):
    global playerX,paused
    paused = False 
    if playerX > 5:
        playerX -=20 
    canvas.moveto(player,playerX,playerY)  
    # =====================moveUp===================== 
def moveUp(event):
    global playerY,paused
    paused = False
    if playerY > 5:
        playerY -=20 
    canvas.moveto(player,playerX,playerY) 
    # =====================moveDown===================== 
def moveDown(event):
    global playerY,paused
    paused = False
    if playerY <590:
        playerY +=20 
    canvas.moveto(player,playerX,playerY) 
    # =====================blood=====================
def blood():
    global  lifeOfPlayer
    x1 = 2
    y1 = 670
    x2 = 42
    y2 = 695
    for blood in range(5):
        if blood >= lifeOfPlayer:
            canvas.create_rectangle(x1,y1,x2,y2,fill='red')
        else:
            canvas.create_rectangle(x1,y1,x2,y2,fill='blue')
        x1 += 40
        x2 += 40  
# =====================display button=====================
canvas.tag_bind("start","<Button-1>", windowPlay)
canvas.tag_bind('back','<Button-1>',goBack)
canvas.tag_bind("exit","<Button-1>", exitFromGame)
canvas.tag_bind("help", "<Button-1>", help)
canvas.tag_bind("help", "<Button-1>", displayHelp) 

canvas.pack()
root.mainloop()
