from tkinter import *
from PIL import Image,ImageTk

GSelect=Tk()
bgIMG=ImageTk.PhotoImage(Image.open("GSelectionIMG.jpg"))
bglabel=Label(GSelect,image=bgIMG)
bglabel.pack()
GSelect.title("Game Selection")
GSelect.geometry("1500x1000")
logoutIMG=ImageTk.PhotoImage(Image.open("LogoutIMG1.jpg"))
logoutbutton=Button(GSelect,image=logoutIMG,bg="black")

SelectLabel=Label(GSelect,text="Choose a Game To Play:",font="times 20",bg="black",fg="Red")
btttIMG=ImageTk.PhotoImage(Image.open("TTTimage.png"))
bTTT=Button(GSelect,image=btttIMG,width=200,height=200)
bTTT.place(x=50,y=120)
SelectLabel.place(x=550,y=50)
logoutbutton.place(x=1200,y=20)
