from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x700")
root.title("Project Game")
canvas = Canvas(root, width=800, height=800)
# =====================image and background=====================
bgStart = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/Project-game/image/bg-start.png"))
bgHelp = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/Project-game/image/rule.png"))

# =====================Start Window=====================
displayHomeBg = True
def displayStart():
    global displayHomeBg
    canvas.delete("all")
    canvas.create_image(0,0, anchor=NW, image = bgStart)
    if displayHomeBg:
        canvas.create_rectangle(300,280,500,330, fill="#09b31d", tags="start", outline="")
        canvas.create_text(400,300, text="Start" ,font=('VNI-Bodon-Poster','25','bold'), fill="white")
        canvas.create_rectangle(300,350,500,400, fill="white", tags="exit", outline="")
        canvas.create_text(400,370, text="Exit" ,font=('VNI-Bodon-Poster','25','bold'))
        canvas.create_rectangle(300,420,500,470, fill="white", tags="help", outline="")
        canvas.create_text(400,440, text="Help" ,font=('VNI-Bodon-Poster','25','bold'),tags='help')
    else:
        gameRull()       
        canvas.create_rectangle(300,600,500,670, fill="white", tags="help", outline="")
        canvas.create_text(400,650,text='BACK',font='Roboto',tags='back')
#=====================back to window=====================
def goBack():
    global displayHomeBg
    displayHomeBg = True        
    print('error')
    displayStart()
canvas.tag_bind('back','<Button-1>',goBack)
# ===================== Display help player to paly this game --------------
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
canvas.tag_bind("exit","<Button-1>", exitFromGame)
canvas.tag_bind("help", "<Button-1>", help)



















# ==================================Create  text help==================================================================
def createHelp():
    canvas.delete('Exit')
    canvas.delete('Start')
    
canvas.tag_bind("help", "<Button-1>", displayHelp)
canvas.pack()
root.mainloop()


