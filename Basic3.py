#แสดงหน้าจอ root
from tkinter import *

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#000000")

#แสดงข้อความ
label1 = Label(root, text="Hello", font=("Arial",30,"bold"), bg="red", fg="white")
label1.pack(fill="x", padx=(20,5), pady=(10,40))

label2 = Label(root, text="World", font=("Arial",30,"bold"), bg="blue", fg="white")
label2.pack(pady=1, ipadx=50, ipady=10)

label3 = Label(root, text="Gui", font=("Arial",30,"bold"), bg="green", fg="white")
label3.pack(fill=BOTH, expand=TRUE)

label4 = Label(root, text="Tkinter", font=("Arial",30,"bold"), bg="black", fg="white")
label4.pack(fill=BOTH, expand=TRUE, ipadx=20, ipady=10)


root.mainloop()  #run program

