from tkinter import *
from PIL import Image, ImageTk     #WE IMPORTED THIS AS TKINTER DOES NOT SUPPORT JPG FILES SO,WITH HELP OF THHIS MODULE WE CAN ADD JPG FILE

aryan_root=Tk()
'''
#FOR TITLE OF OUR GUI
aryan_root.title("MY FIRST GUI")

#Widht x Height (GEO. WILL BE IN "" AS IT'S CONSTANT
aryan_root.geometry("337x443")

#Widht , Height
aryan_root.minsize(200,100)

#Width ,Height
aryan_root.maxsize(1000,700)

aryan=Label(text="Hello!WELCOME TO PYCHARM")
#IMPORTANT GUI
# text - adds the text
# bg - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

'''
_label=Label(text='''
A GUI (graphical user interface) is a system of interactive visual components for computer software.
 A GUI displays objects that convey information, and represent actions that can be taken by the user.
The objects change color, size, or visibility when the user interacts with them.''',
bg="orange",fg="green",font=("comicsansms", 19, "bold"),padx="96",pady="69",relief=SUNKEN)
_label.pack()
'''000
'''


aryan_root.geometry("1098x480")


#for png
#photo=PhotoImage(file="1.png")

#for JPG and etc.. -  from PIL import Image, ImageTk
image=Image.open("file.jpeg")
photo=ImageTk.PhotoImage(image)

aryan_label=Label(image=photo,text="Yeh kya ho rha hy")
aryan_label.pack()

#TYPES OF PACK
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

aryan_root.mainloop()