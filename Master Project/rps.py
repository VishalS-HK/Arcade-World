from tkinter import *
import random
from tkinter.messagebox import showinfo

#window
window=Tk()
window.geometry('800x500')
window.title('Rock Paper Scissor!!')
title=Label(frame4,text='\n Rock Paper Scissor!! \n',fg='grey')
title.config(font=('Courier',40))
title.grid(row=0,column=2,columnspan=5)

def rpsgame():
    computer_input=""
    playercounter=0
    computercounter=0
    frame4=Frame(window)


    title2=Label(frame4,text='Enjoy the game......\n \n',fg='green')
    title2.config(font=('Courier',20))
    title2.grid(row=1,column=3)
    #insertframe=Frame(window)
    #insertframe.pack()

    options=Label(frame4,text='Options:\n',fg='orange')
    options.config(font=('Courier',18))
    options.grid(row=3,column=1)



    opt=['rock','paper','scissor']
    def winner(player_input):
        global your_score,computer_score,computer_input,playercounter,computercounter
        computer_input=random.choice(opt)
        
        if player_input==computer_input:
            title2.config(text="It is a Tie!")
            computer_choice.config(text="Computer's choice-->"+computer_input)
            your_choice.config(text="Your choice-->"+player_input)
        elif (player_input=="rock" and computer_input=="paper") or (player_input=="scissor" and computer_input=="rock") or (player_input=="paper" and computer_input=="scissor"):
            title2.config(text="Computer won!")
            computercounter+=1
            computer_choice.config(text="Computer's choice-->"+computer_input)
            your_choice.config(text="Your choice-->"+player_input)
            computer_score.config(text="Computer's Score-->"+str(computercounter))
        else:
            title2.config(text="You win!")
            playercounter+=1
            your_score.config(text="Your Score-->"+str(playercounter))
            computer_choice.config(text="Computer's choice-->"+computer_input)
            your_choice.config(text="Player choice-->"+str(player_input))

        

    #buttons
    rock=Button(frame4,text='ROCK',width=15,command=lambda:winner("rock"))
    rock.grid(column=2,row=4)

    paper=Button(frame4,text='PAPER',width=15,command=lambda:winner("paper"))
    paper.grid(row=4,column=3)

    scissor=Button(frame4,text='SCISSOR',width=15,command=lambda:winner("scissor"))
    scissor.grid(row=4,column=4)

    your_choice=Label(frame4,text='Your choice-->(playername)')
    your_choice.grid(row=6, column=1)

    #results
    your_score=Label(frame4,text=f'''Your Score-->{playercounter}''')
    your_score.grid(row=6,column=3)

    computer_choice=Label(frame4,text=f'''Computer's choice-->{computer_input}''')
    computer_choice.grid(row=7,column=1)

    computer_score=Label(frame4,text=f'''Computer's Score-->{computercounter}''')
    computer_score.grid(row=7,column=3)
    frame4.pack()
    window.mainloop()
