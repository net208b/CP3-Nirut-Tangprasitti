from tkinter import *
import math

def leftclickbutton(event):
    labelresult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    check = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if check >= 30:
        result = "อ้วนมาก"
    elif 25 <= check <= 29.9:
        result = "อ้วน"
    elif 23 <= check <= 24.9:
        result = "น้ำหนักเกิน"
    elif 18.6 <= check <= 22.9:
        result = "น้ำหนักปกติ"
    elif check <= 18.5:
        result = "ผอมเกิน"
    labelresult1.configure(text = result)


mainwindow = Tk()
labelHeight = Label(mainwindow, text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainwindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainwindow, text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainwindow)
textBoxWeight.grid(row=1,column=1)
calculatebutton = Button(mainwindow,text = "คำนวณ")
calculatebutton.bind('<Button-1>', leftclickbutton)
calculatebutton.grid(row =2,column=0)
labelresult = Label(mainwindow,text="ผลลัพธ์")
labelresult.grid(row=2,column=1)
labelresult1 = Label(mainwindow,text="ผลลัพธ์")
labelresult1.grid(row=3,column=1)

mainwindow.mainloop()