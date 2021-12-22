from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x700")
root.title("Project Game")
canvas = Canvas(root, width=800, height=800)
image = ImageTk.PhotoImage(Image.open("C:\\Users\Student\Desktop\Project-game\image\\bg-start.png"))
# canvas.create_image(0,0, anchor=NW, image = image)

# --------Start Window
toStart = True
def displayStart():
    global toStart
    canvas.delete("all")
    canvas.create_image(0,0, anchor=NW, image = image)
    if toStart:
        canvas.create_rectangle(300,280,500,330, fill="#09b31d", tags="start", outline="")
        canvas.create_text(400,300, text="Start" ,font=('VNI-Bodon-Poster','25','bold'), fill="white")
        canvas.create_rectangle(300,350,500,400, fill="white", tags="exit", outline="")
        canvas.create_text(400,370, text="Exit" ,font=('VNI-Bodon-Poster','25','bold'))
        canvas.create_rectangle(300,420,500,470, fill="white", tags="help", outline="")
        canvas.create_text(400,440, text="Help" ,font=('VNI-Bodon-Poster','25','bold'))
        print("yes")
    else:
        print("no")
displayStart()

def displayHelp():
    canvas.create_text(30, 40, text="1. User musthe\nheafhdoeiofaoifodifai\nehrahhaithahaihtia",font=("VNI-Bodon-Poster","20"))
    
displayHelp()
# ----------------- Display help player to paly this game --------------
def exitFromGame():
    root.destroy()

def help(event):
    global toStart
    toStart = False
    displayStart()
canvas.tag_bind("exit","<Button-1>", exitFromGame)
canvas.tag_bind("help", "<Button-1>", help)



















canvas.pack()
root.mainloop()


