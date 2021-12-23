from tkinter import *
from tkinter import font
import winsound
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x800")
root.title("Project Game")
canvas = Canvas(root, width=800, height=800)
# winsound.PlaySound('.\sound\start-game.wav', winsound.SND_FILENAME)
# =====================image and background=====================
bgStart = ImageTk.PhotoImage(Image.open("image/bg-start.png"))
bgHelp = ImageTk.PhotoImage(Image.open("image/rule.png"))
startGame =ImageTk.PhotoImage(Image.open('image/bg-play.png'))
# =====================variable=====================
displayHomeBg = True    
# =====================sound=====================

# =====================Start Window=====================

def displayStart():
    global displayHomeBg
    canvas.delete("all")
    canvas.create_image(0,0, anchor=NW, image = bgStart)
    
    if displayHomeBg:
        # ===========start===========
        canvas.create_rectangle(300,280,500,330, fill="#09b31d", tags="start", outline="")
        canvas.create_text(400,305, text="Start" ,font=('VNI-Bodon-Poster','25','bold'), fill="white",tags='start')
        # ===========Exit===========
        canvas.create_rectangle(300,350,500,400, fill="white", tags="exit", outline="")
        canvas.create_text(400,375, text="Exit" ,font=('VNI-Bodon-Poster','25','bold'),tags='exit')
        # ===========Help===========
        canvas.create_rectangle(300,420,500,470, fill="white", tags="help", outline="")
        canvas.create_text(400,444, text="Help" ,font=('VNI-Bodon-Poster','25','bold'),tags='help')
    else:
        gameRull()       
        canvas.create_rectangle(300,600,500,670, fill="white", tags="help", outline="")
        canvas.create_text(400,635,text='BACK',font=('Roboto','23','bold'),tags='back')
#=====================start game =====================
def startGame(event):
    canvas.delete('all')
    canvas.create_image(0,0, anchor=NW,image=startGame)
    canvas.create_text(400,500,text='How are you?')
    
    
#=====================back to window=====================
def goBack(event):
    global displayHomeBg
    displayHomeBg = True        
    displayStart()
# ===================== Display help player to paly this game =====================
def exitFromGame(event):
    root.destroy()

displayStart()
def gameRull():
    canvas.delete("all")
    canvas.create_image(0,0, anchor=NW, image = bgHelp)
# =====================click help=====================
def displayHelp(event):
    global displayHomeBg
    displayHomeBg = False
    displayStart()
# =====================display sound=====================
# def displaySound():   

canvas.tag_bind('start','<Button-1>',startGame)
canvas.tag_bind('back','<Button-1>',goBack)
canvas.tag_bind("exit","<Button-1>", exitFromGame)
canvas.tag_bind("help", "<Button-1>", help)



















# ==================================Create  text help==================================================================
def createHelp():
    canvas.delete('Exit')
    canvas.delete('Start')
    
canvas.tag_bind("help", "<Button-1>", displayHelp)
canvas.pack()
root.mainloop()


