#แสดงหน้าจอ root
from tkinter import *
import tkinter.messagebox

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

def selectChoice():
    result = choice.get()
    if result == 1:
        root.config(bg="green")
    elif result == 2:
        root.config(bg="pink")
    else:
        root.config(bg="purple")

choice = IntVar()
# radio button
Radiobutton(root, text="green", value=1, variable=choice, command=selectChoice).grid(row=0, column=0)
Radiobutton(root, text="pink", value=2, variable=choice, command=selectChoice).grid(row=0, column=1)
Radiobutton(root, text="blue", value=3, variable=choice, command=selectChoice).grid(row=0, column=2)

root.mainloop()