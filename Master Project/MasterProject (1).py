from tkinter import *
from tkinter.messagebox import showinfo,askyesno
from tkinter.simpledialog import askstring
import mailing as em
from PIL import Image,ImageTk

global cb,cbrpe,cbrcpe

def Gameon(back_buttonIMG):
    
    frame2.pack_forget()
    frame3=Frame(RorL,bg="black")
    RorL.title("Tic-Tac-Toe Game")
    numbers=[1,2,3,4,5,6,7,8,9]
    # y='X' for player1 and 'O' for player2
    y=""
    # x is the counter to keep counting the number of chances
    x=0
    #boards is a list to store the mark with respect to the cell number
    boards=[""]*10
    counter1=0
    counter2=0

    def reset():
        nonlocal boards,numbers,x,y,counter1,counter2
        x=0
        y=""
        boards=[""]*10
        numbers=[1,2,3,4,5,6,7,8,9]
        counterlabel1.config(text=f'''Player 1 Score:{counter1}''')
        counterlabel2.config(text=f'''Player 2 Score:{counter2}''')
        for i in numbers:
            lb[i-1].config(text="")
     
    def result(boards,mark):
        return ((boards[1] == boards[2] == boards [3] == mark) 
                or (boards[4] == boards[5] == boards [6] == mark) 
                or (boards[7] == boards[8] == boards [9] == mark) 
                or (boards[1] == boards[4] == boards [7] == mark) 
                or (boards[2] == boards[5] == boards [8] == mark)
                or (boards[3] == boards[6] == boards [9] == mark)
                or (boards[1] == boards[5] == boards [9] == mark) 
                or (boards[3] == boards[5] == boards [7] == mark))
                
    def decider(a,b,n):
            nonlocal x,y,numbers,counter1,counter2
            x,y,num=a,b,n
            if x%2==0:
                y='X'
                boards[num]=y
            elif x%2!=0:
                y='O'
                boards[num]=y
            lb[num-1].config(text=y) #Display X or O on the button clicked by user
            x=x+1
            mark=y
            # Here we are calling the result() to decide whether we have got the winner or not
            if(result(boards,mark) and mark=='X' ):
                #If Player1 is the winner show a dialog box stating the winner
                showinfo("Result","Player 1 wins")
                counter1+=1
                #Call the destroy function to close the GUI
                reset()
            elif(result(boards,mark) and mark=='O'):
                showinfo("Result","Player 2 wins")
                counter2+=1
                reset()
     
    def click(num):
        nonlocal x,y,numbers
        """ To Check which button has been clicked to avoid over-writing"""
        if num in numbers:
            numbers.remove(num)
            decider(x,y,num)
                 
        # If we have not got any winner, display match has been tied.
        if(x>8 and result(boards,'X')==False and result(boards,'O')==False):
            showinfo("Result","Match Tied")
            reset()

    backbutton=Button(frame3,image=back_buttonIMG,command=lambda:frame3.destroy())
    backbutton.grid(row=1,column=1)
    counterlabel1=Label(frame3,text="Player 1 Score:0")
    counterlabel1.grid(row=2,column=1)
    counterlabel2=Label(frame3,text="Player 2 Score:0")
    counterlabel2.grid(row=3,column=1)
    l1=Label(frame3,text=" player1 : X",font="times 18")
    l1.grid(row=0,column=1)
    l2=Label(frame3,text=" player2 : O",font="times 18")
    l2.grid(row=0,column=2)
     # combined building buttons and gridding the button
    b1=Button(frame3,width=20,height=10,command=lambda:click(1))
    b1.grid(row=1,column=6)
    b2=Button(frame3,width=20,height=10,command=lambda:click(2))
    b2.grid(row=1,column=7)
    b3=Button(frame3,width=20,height=10,command=lambda: click(3))
    b3.grid(row=1,column=8)
    b4=Button(frame3,width=20,height=10,command=lambda: click(4))
    b4.grid(row=2,column=6)
    b5=Button(frame3,width=20,height=10,command=lambda: click(5))
    b5.grid(row=2,column=7)
    b6=Button(frame3,width=20,height=10,command=lambda: click(6))
    b6.grid(row=2,column=8)
    b7=Button(frame3,width=20,height=10,command=lambda: click(7))
    b7.grid(row=3,column=6)
    b8=Button(frame3,width=20,height=10,command=lambda: click(8))
    b8.grid(row=3,column=7)
    b9=Button(frame3,width=20,height=10,command=lambda: click(9))
    b9.grid(row=3,column=8)
    lb=[b1,b2,b3,b4,b5,b6,b7,b8,b9] #Storing buttons in a list to reduce code size
    
    frame3.pack(expand=1)


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
                    frame1.pack_forget()
                else:
                    s="\n"+b+","+a+","+c
                    fw.write(s)
                    fw.close()
                    frame1.pack_forget()


                    
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
                        frame1.pack_forget()
                        RorL.title("Game Selection")
                else:
                    frame1.pack_forget()
                    RorL.title("Game Selection")
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


#showpass        
def showpass():
    if cb.var.get():
        lpe.config(show="*")
    else:
        lpe.config(show="")
def showpass2():
    if cbrpe.var.get():
        rpe.config(show="*")
    else:
        rpe.config(show="")
def showpass3():
    if cbrcpe.var.get():
        rcpe.config(show="*")
    else:
        rcpe.config(show="")
        
RorL=Tk()
RorL.title("Welcome to the Game terminal")
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
cbrpe=Checkbutton(frame1,text="Show Password",onvalue=False,offvalue=True,command=showpass2)
cbrpe.var=BooleanVar(value=True)
cbrpe['variable']=cbrpe.var
cbrpe.place(x=400,y=360)
cbrcpe=Checkbutton(frame1,text="Show Password",onvalue=False,offvalue=True,command=showpass3)
cbrcpe.var=BooleanVar(value=True)
cbrcpe['variable']=cbrcpe.var
cbrcpe.place(x=400,y=450)

rme=Entry(frame1,width=30)
rne=Entry(frame1,width=30)
rml.place(x=400,y=200)
rme.place(x=400,y=225)
rnl.place(x=400,y=250)
rne.place(x=400,y=275)
rpl.place(x=400,y=300)
rpe.place(x=400,y=325)
rcpl.place(x=400,y=390)
rcpe.place(x=400,y=415)
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
register=Button(frame1,text="Register",width=10,height=2,bg="green",command=lambda:registration(rme.get(),rne.get(),rpe.get(),rcpe.get() if rme.get()!="" and rne.get()!="" and rpe.get()!="" and rcpe.get()!="" else showinfo("Please fill everything"))) #mail#name#pass#confirmpass
login=Button(frame1,text="Login",width=10,height=2,bg="green",command=lambda:Login(lme.get(),lpe.get()) if lme.get()!="" and lpe.get()!="" else showinfo("Please enter all the classifields") )
forgotpass=Button(frame1,text="Forgot Password",width=12,height=1,bg="yellow",command=lambda:fpass())
forgotpass.place(x=900,y=300)
register.place(x=400,y=480)
login.place(x=750,y=325)
rb.place(x=400,y=100)
lb.place(x=750,y=100)
cb=Checkbutton(frame1,text="Show Password",onvalue=False,offvalue=True,command=showpass)
cb.var=BooleanVar(value=True)
cb['variable']=cb.var
cb.place(x=760,y=300)
frame1.pack()

frame2=Frame(RorL)
bgIMG=ImageTk.PhotoImage(Image.open("GSelectionIMG.jpg"))
bglabel=Label(frame2,image=bgIMG)
bglabel.pack()
logoutIMG=ImageTk.PhotoImage(Image.open("LogoutIMG1.jpg"))
logoutbutton=Button(frame2,image=logoutIMG,bg="black",command=lambda:frame2.destroy())
SelectLabel=Label(frame2,text="Choose a Game To Play:",font="times 20",bg="black",fg="Red")
btttIMG=ImageTk.PhotoImage(Image.open("TTTimage.png"))
back_buttonIMG=ImageTk.PhotoImage(Image.open("back_buttonIMG.jpg"))
bTTT=Button(frame2,image=btttIMG,width=200,height=200,command=lambda:Gameon(back_buttonIMG))
bTTT.place(x=50,y=120)
SelectLabel.place(x=550,y=50)
logoutbutton.place(x=1200,y=20)
frame2.pack()

RorL.mainloop()

