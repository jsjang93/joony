# gui01.py
# Python GUI --> tkinter, wxPython,PyQt
# 위젯 (Button,Label,Entry,,,,)
from tkinter import *

def btn1Click():
    text1.insert(0,text1.get()+"님 어서오세요!    ")

window = Tk()
#################
label1  = Label(window,text="이 름")
label1.grid(row=0,column=0)
#label1.pack()

text1 = Entry(window)
text1.grid(row=0,column=1)
#text1.pack()

button1 = Button(window, bg="yellow",text="입 력",command=btn1Click)
#button1["fg"] = "yellow"
#button1["bg"] = "red"
button1.grid(row=1,column=1)
#button1.pack()

#################
window.mainloop()  # 이거하면 계속 떠있음

