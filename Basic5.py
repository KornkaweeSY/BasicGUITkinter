#แสดงหน้าจอ root
from tkinter import *

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

btn1 = Button(root, text="ปุ่มที่ 1")
btn1.pack(side=TOP)

btn2 = Button(root, text="ปุ่มที่ 2", bg="blue", fg="white")
btn2.pack(side=LEFT)

btn3 = Button(root, text="ปุ่มที่ 3", bg="green", fg="white")
btn3.pack(side=RIGHT)

btn4 = Button(root, text="ปุ่มที่ 4", bg="black", fg="white", activebackground="white", activeforeground="red")
btn4.pack(side=BOTTOM)



root.mainloop()  #run program

