#แสดงหน้าจอ root
from tkinter import *
import tkinter.messagebox

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

def showName():
    name = userName.get()
    if name == "":
        tkinter.messagebox.showerror("รายละเอียด", "กรุณาป้อนข้อมูล")
        
    else:
        myText.delete(0, END)
        tkinter.messagebox.showinfo("รายละเอียด", "ผู้ใช้งานโปรแกรม = " + name)

def quitProgram():
    confirm = tkinter.messagebox.askquestion("ยืนยัน", "คุฯต้องการปิดโปรแกรมหรือไม่?")
    if confirm == "yes":
        root.destroy()

# entry widget
userName = StringVar() # save data in entry widget

myText = Entry(root, width="40", font=('Arail', 25), textvariable=userName)
myText.pack(pady=10, padx=10)
btnSave = Button(root, text="Save", fg="black", bg="white", command=showName)
btnSave.pack(ipadx=30, ipady=10)

btnQuit = Button(root, text="ออกจากโปรแกรม", fg="white", bg="purple", command=quitProgram)
btnQuit.pack(ipadx=10, ipady=10, padx=5, pady=5)

root.mainloop()