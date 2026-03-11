from tkinter import *
from gpiozero import Button
BTN_CLOSEAPP = 27
wnd = Tk()
wnd.title("Button test")
wnd.geometry("400x200+200+200")

def tb_pressed():
    print("Button pressed")
    label_button.config(text="Button was pressed")

close_button = Button(BTN_CLOSEAPP,pull_up=True)
#close_button.when_pressed = tb_pressed
close_button.when_pressed = lambda: wnd.destroy()
label_button = Label(wnd,text="Wait for button")

label_button.pack()
wnd.mainloop()