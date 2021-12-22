
import tkinter as tk
root = tk.Tk()
frame = tk.Frame()
canvas = tk.Canvas(frame)
# bgImage = tk.PhotoImage(file='image/bg.jpg')
root.geometry("1240x1024")

canvas.pack(expand=True,fill="both")
frame.pack(expand= True, fill="both")
root.mainloop()


