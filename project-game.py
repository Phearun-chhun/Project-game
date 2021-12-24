from tkinter import *
from tkinter import font
import random
from types import BuiltinFunctionType
import winsound
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

# =====================variable=====================
x1 = 2
y1 = 670
x2 = 42
y2 = 695
lifeOfPlayer = 5
displayHomeBg = True
displayPlayBg = False
listBulletOfPlayer = []
listOfEnemy  = []
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
    global displayHomeBg, displayPlayBg
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
        canvas.create_rectangle(30,30,70,70, fill="red")
        canvas.create_image(50,50,image=enemyIamge)
        canvas.create_rectangle(300,420,500,470, fill="white", tags="help", outline="")
        canvas.create_text(400,444, text="Help" ,font=('VNI-Bodon-Poster','25','bold'),tags='help')
        winsound.PlaySound('sound\start-game.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)

    elif displayPlayBg:
        canvas.create_image(0,0, anchor=NW, image = bgPlay)
        canvas.create_text(700,685,text='Score: ',font=('Roboto','22','bold'),fill='white')
        blood()
    else:
        gameRule()       
        canvas.create_rectangle(300,600,500,670, fill="white", tags="help", outline="")
        canvas.create_text(400,635,text='BACK',font=('Roboto','23','bold'),tags='back')    
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
    global displayPlayBg, displayHomeBg
    displayPlayBg = True
    displayHomeBg = False
    displayBackground()
    createEnemy()
    moveEnemy()
    createPlayer()
    moveBullet()
    # createBullet(event)

# =====================create enemies=====================
def createEnemy():
    if len(listOfEnemy)<8:
        enemy = canvas.create_image(random.randrange(20,650),-50,anchor = NW,image=enemyIamge)

        listOfEnemy.append(enemy)
    canvas.after(1000,createEnemy)
# =====================move enemy=====================    
def moveEnemy():
    global listOfEnemy
    deleteEnemy = []
    for enemies in listOfEnemy:
        canvas.move(enemies,0,12)
        position  = canvas.coords(enemies)
        if position[1] > 620:
            deleteEnemy.append(enemies)
    for enemies in deleteEnemy:
        listOfEnemy.remove(enemies)
        canvas.delete(enemies)
    canvas.after(100,moveEnemy)


            
    # =====================create player=====================
def createPlayer():
    global player, playerX, playerY
    player = canvas.create_image(playerX,playerY,anchor = NW, image= playerImage)


#  =====================createBullet=====================
def createBullet(event):
    global playerX, playerY,bulletOfPlayer,listBulletOfPlayer
    bulletOfPlayer = canvas.create_image(playerX+48,playerY, image=playerBullet,tags= 'player-bullet')
    listBulletOfPlayer.append(bulletOfPlayer)
#     =====================moveBullet=====================
def moveBullet():
    global bulletOfPlayer,listBulletOfPlayer,py
    delletBulletPlayer = []
    for bulletOfPlayer in listBulletOfPlayer:
        canvas.move(bulletOfPlayer,0,-20)
        position  = canvas.coords(bulletOfPlayer)
        py = position[1]
        if position[1] <20 :
            delletBulletPlayer.append(bulletOfPlayer)
    for bulletOfPlayer in delletBulletPlayer:
        if position[1] <0 :           
            listBulletOfPlayer.remove(bulletOfPlayer)
            canvas.delete(bulletOfPlayer)
    canvas.after(50,moveBullet)





    
# Move player ==============================
    # =====================moveRight=====================
def moveRight(event):
    global playerX,paused,playerY
    paused = False
    if playerX < 670:
        playerX +=10 
    canvas.moveto(player,playerX,playerY)
    # =====================moveLeft===================== 
def moveLeft(event):
    global playerX,paused
    paused = False
    if playerX > 5:
        playerX -=10 
    canvas.moveto(player,playerX,playerY)  
    # =====================moveUp===================== 
def moveUp(event):
    global playerY,paused
    paused = False
    if playerY > 5:
        playerY -=10 
    canvas.moveto(player,playerX,playerY) 
# =====================moveDown===================== 
def moveDown(event):
    global playerY,paused
    paused = False
    if playerY <590:
        playerY +=10 
    canvas.moveto(player,playerX,playerY) 
# =====================blood=====================
def blood():
    global x1, x2,y1,y2, lifeOfPlayer
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
root.bind('<f>',moveRight)
root.bind('<s>',moveLeft)
root.bind('<e>',moveUp)
root.bind('<d>',moveDown)
root.bind('<a>',createBullet)
canvas.pack()
root.mainloop()


