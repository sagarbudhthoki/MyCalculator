from tkinter import*
import math
import configparser
import tkinter.messagebox
root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc= Frame(root)
calc.grid()

menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="standard")
filemenu.add_command(label="Scientific")
filemenu.add_separator()
filemenu.add_command(label="Exit")
root.config(menu=menubar)
root.mainloop()

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=filemenu)
filemenu.add_command(label="Cut")
filemenu.add_command(label="Copy")
filemenu.add_separator()
filemenu.add_command(label="paste")
