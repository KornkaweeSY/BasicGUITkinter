#แสดงหน้าจอ root
from tkinter import *
from tkinter.filedialog import *

root = Tk() #main window
root.title("Test")
root.iconbitmap("icons/logo.ico")
root.geometry("400x300+750+300")
#root.resizable(0,0) #ใช่สำหรับไม่ให้ปรับบขนาด window
root.config(bg="#ffffff")

def selectFile():
    fileopen = askopenfilename(title="เปิดไฟล์", initialdir="./", filetypes=(("Text File", "*.txt"), ("ALL File", "*")))
    # print(fileopen)

    with open(fileopen, "r", encoding="utf8") as f:
        # print(f.read())
        Label(root, text = f.read()).pack()

btn1 = Button(root, text="เลือกไฟล์", command=selectFile).pack()

root.mainloop()