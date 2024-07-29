from tkinter import *

def buttonpress(num):
    pass

def equal():
    pass

def clear():
    pass 

window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()    


window.mainloop()
