#แสดงหน้าจอ root
from tkinter import *

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

btn1 = Button(root, text="ปุ่มที่ 1")
btn1.grid(row=0,column=0, padx=5, pady=5, ipadx=10, ipady=10)

btn2 = Button(root, text="ปุ่มที่ 2", bg="blue", fg="white")
btn2.grid(row=0,column=1, padx=5, pady=5, ipadx=10, ipady=10)

btn3 = Button(root, text="ปุ่มที่ 3", bg="green", fg="white")
btn3.grid(row=0,column=2, padx=5, pady=5, ipadx=10, ipady=10)

btn4 = Button(root, text="ปุ่มที่ 4", bg="black", fg="white", activebackground="white", activeforeground="red")
btn4.grid(row=1,column=0, padx=5, pady=5, ipadx=10, ipady=10)

btn5 = Button(root, text="ปุ่มที่ 5", bg="black", fg="white", activebackground="white", activeforeground="red")
btn5.grid(row=1,column=1, padx=5, pady=5, ipadx=10, ipady=10)

btn6 = Button(root, text="ปุ่มที่ 6", bg="black", fg="white", activebackground="white", activeforeground="red")
btn6.grid(row=1,column=2, padx=5, pady=5, ipadx=10, ipady=10)



root.mainloop()  #run program

