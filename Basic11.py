#แสดงหน้าจอ root
from tkinter import *
from PIL import ImageTk, Image

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

# read image
img1 = ImageTk.PhotoImage(Image.open("Image/programmer.png"))
Label(root, image = img1).pack()


root.mainloop()  #run program