from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x700")
root.title("Project Game")
canvas = Canvas(root, width=800, height=800)
image = ImageTk.PhotoImage(Image.open("C:\\Users\Student\Desktop\Phearun\Project-game\image\\bg-start.png"))
canvas.create_image(0,0, anchor=NW, image = image)

# --------Start Window
toStart = True
def displayStart():
    global toStart
    canvas.delete("exitbg")
    canvas.delete("startbg")
    if toStart:
        canvas.create_rectangle(250,280,550,330, fill="#09b31d", tags="startbg")
        canvas.create_text(400,300, text="Start" ,font=('VNI-Bodon-Poster','30','bold'), fill="white")
        canvas.create_rectangle(250,350,550,400, fill="white", tags="exitbg")
        canvas.create_text(400,370, text="Exit" ,font=('VNI-Bodon-Poster','30','bold'))
        canvas.create_rectangle(250,420,550,470, fill="white", tags="help")
        canvas.create_text(400,440, text="Help" ,font=('VNI-Bodon-Poster','30','bold'))
        print("yes")
    else:
        canvas.create_rectangle(250,420,550,470, fill="white", tags="help")
        canvas.create_text(400,440, text="Help" ,font=('VNI-Bodon-Poster','30','bold'),tags="help")
        print("no")
displayStart()
# click help
def displayHelp(event):
    global toStart
    # root.destroy()
    print("hello")
    toStart = False
    displayStart()
# ==================================Create  text help==================================================================
def createHelp():
    canvas.delete('Exit')
    canvas.delete('Start')
    
canvas.tag_bind("help", "<Button-1>", displayHelp)
canvas.pack()
root.mainloop()


