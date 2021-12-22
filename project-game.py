from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x700")
canvas = Canvas(root, width=800, height=800)
image = ImageTk.PhotoImage(Image.open("C:\\Users\Student\Desktop\Project-game\image\\bg-start.png"))
canvas.create_image(0,0, anchor=NW, image = image)
canvas.pack()
root.mainloop()


