from tkinter import *
from  PIL import ImageTk,Image
aryan=Tk()
aryan.geometry("1010x1080")
aryan.title("NEWSPAPER")

image=Image.open("file.jpeg")
photo=ImageTk.PhotoImage()
__label=Label(photo)
__label.pack
aryan.mainloop()