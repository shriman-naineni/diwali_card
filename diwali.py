from tkinter import *

screen = Tk()
screen.title("Greeting Card")
screen.geometry("800x800")

font_1 = ("Times","100", "bold italic")

name = Label(screen, text = "HAPPY DIWALI", font = font_1)
name.pack()

screen.mainloop()