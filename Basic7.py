#แสดงหน้าจอ root
from tkinter import *

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

# create frame
frame1 = Frame(root, bg="pink")
frame2 = LabelFrame(root, text="Frame title")

# show frame

frame1.pack(fill=BOTH, expand=TRUE)
Button(frame1, text="Button 1").pack()
Button(frame1, text="Button 2").pack()
Button(frame1, text="Button 3").pack()

frame2.pack(fill=BOTH, expand=TRUE)
Button(frame2, text="Button 4").grid(row=0,column=0)
Button(frame2, text="Button 5").grid(row=0,column=1)
Button(frame2, text="Button 6").grid(row=0,column=2)

root.mainloop()