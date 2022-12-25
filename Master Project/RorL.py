from tkinter import *
from tkinter.messagebox import showinfo,askyesno
from tkinter.simpledialog import askstring
import mailing as em
import TTT
from PIL import Image,ImageTk

def registration(a,b,c,d):
    f=open("UserDataBase.txt")
    content=(f.read().splitlines())
    fw=open("UserDataBase.txt","a")
    for m in content:
        x=m.split(",")
        if c!=d:
            showinfo("Incorrect Input","Password and Confirm Password is different!")
            break
        if a==x[1]:
            showinfo("Alert!","An account using the provided email already exists\n\tYou can try logging in!")
            break
        else:
            authentication=em.welcome(a,b)
            code=askstring("Mail confirmation","Please enter confirmation code that was mailed to you")
            if code==authentication:
                response=askyesno("Real Quick!","Would you like to enable 2FA and make your account more secure?")
                if response=="Yes":
                    s="\n"+b+","+a+","+c+",2FA"
                    fw.write(s)
                    fw.close()
                    frame1.destroy()
                else:
                    s="\n"+b+","+a+","+c
                    fw.write(s)
                    fw.close()
                    frame1.destroy()
                    
def Login(a,b):
    f=open("UserDataBase.txt","r")
    content=(f.read()).splitlines()
    c=1
    for m in content:
        x=m.split(",")
        if a==x[1]:
            c=0
            if b==x[2]:
                if "2FA" in m:
                    authentication=em.two_FA(a,x[0])
                    code=askstring("2FA confirmation","Please enter the 6-digit 2FA code that was mailed to you")
                    if code==authentication:
                        frame1.destroy()
                else:
                    frame1.destroy()
            else:
                showinfo("Wrong password","The password you have entered is wrong")
                break
    if c!=0:
        showinfo("Wrong email","The email you provided hasn't registered an account\n\tYou can try registering a new account!")

def fpass():
    a=askstring("Forgot Password","Please enter your email address")
    f=open("UserDataBase.txt","r")
    content=(f.read()).splitlines()
    fw=open("UserDataBase.txt","a")
    c=1
    l=f.read()
    for m in content:
        x=m.split(",")
        if a==x[1]:
            c=0
            authentication=em.change_pass(a,x[0])
            l=l.replace(x[2],authentication)
            fw.writelines(l)
            fw.close()
            
    if c!=0:
        showinfo("Wrong Email","There is no Game account in the mail you specified!")

RorL=Tk()
RorL.title("Welcome to Tic Tac Toe game")
RorL.geometry("1500x1000")
frame1=Frame(RorL)
bgimg=ImageTk.PhotoImage(Image.open("RorLBGI.jpg"))
bglabel=Label(frame1,image=bgimg)
bglabel.pack()
rml=Label(frame1,text="Enter your email address:")
rnl=Label(frame1,text="Enter your name:")
rpl=Label(frame1,text="Enter your Password")
rcpl=Label(frame1,text="Confirm your Password")
rpe=Entry(frame1,width=30,show="*")
rcpe=Entry(frame1,width=30,show="*")
rme=Entry(frame1,width=30)
rne=Entry(frame1,width=30)
rml.place(x=400,y=200)
rme.place(x=400,y=225)
rnl.place(x=400,y=250)
rne.place(x=400,y=275)
rpl.place(x=400,y=300)
rpe.place(x=400,y=325)
rcpl.place(x=400,y=350)
rcpe.place(x=400,y=375)
lml=Label(frame1,text="Enter your email address:")
lml.place(x=750,y=200)
lme=Entry(frame1,width=30)
lme.place(x=750,y=225)
lpl=Label(frame1,text="Enter your Password")
lpl.place(x=750,y=250)
lpe=Entry(frame1,width=30,show="*")
lpe.place(x=750,y=275)
Registerbg=ImageTk.PhotoImage(Image.open("RegisterIMG.png"))
Loginbg=ImageTk.PhotoImage(Image.open("LoginIMG.jpg"))
rb=Label(frame1,image=Registerbg)
lb=Label(frame1,image=Loginbg)                                      
register=Button(frame1,text="Register",width=10,height=2,bg="green",command=lambda:registration(rme.get(),rne.get(),rpe.get(),rcpe.get())) #mail#name#pass#confirmpass
login=Button(frame1,text="Login",width=10,height=2,bg="green",command=lambda:Login(lme.get(),lpe.get()))
forgotpass=Button(frame1,text="Forgot Password",width=12,height=1,bg="yellow",command=lambda:fpass())
forgotpass.place(x=840,y=300)
register.place(x=400,y=400)
login.place(x=750,y=325)
rb.place(x=400,y=100)
lb.place(x=750,y=100)
frame1.pack()

frame2=Frame(RorL)
bgIMG=ImageTk.PhotoImage(Image.open("GSelectionIMG.jpg"))
bglabel=Label(frame2,image=bgIMG)
bglabel.pack()
logoutIMG=ImageTk.PhotoImage(Image.open("LogoutIMG1.jpg"))
logoutbutton=Button(frame2,image=logoutIMG,bg="black")
SelectLabel=Label(frame2,text="Choose a Game To Play:",font="times 20",bg="black",fg="Red")
btttIMG=ImageTk.PhotoImage(Image.open("TTTimage.png"))
bTTT=Button(frame2,image=btttIMG,width=200,height=200,command=lambda:TTT.Gameon())
bTTT.place(x=50,y=120)
SelectLabel.place(x=550,y=50)
logoutbutton.place(x=1200,y=20)
frame2.pack()

RorL.mainloop()
