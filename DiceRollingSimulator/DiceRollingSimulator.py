from tkinter import *
from tkinter import messagebox as ms
import random as rnd 


def Exit():
    gameWindow.destroy()

def DiceRolling():

    j = 130
    for i in range(0,diceNumber.get()):
        temp = rnd.randint(1,6)
        label0 = Label(gameWindow,text = "{}. Dice".format(i+1),width=20,font=("bold",10))
        label0.place(x=150,y=j)
        label1 = Label(gameWindow,text = temp,width=10,font=("bold",10))
        label1.place(x=260,y=j)
        j += 30
        
       


def gameStarting():
    global gameWindow
    gameWindow = Tk()
    gameWindow.title("Dice Rolling Simulator")
    gameWindow.geometry("600x400+500+100")

    label0 = Label(gameWindow,text = "Dice Rolling Simulator",width=20,font=("bold",20))
    label0.place(x=110,y=53)

    DiceRolling()
    Button(gameWindow,text='Dice Rolling',command=DiceRolling,width=20,bg='brown',fg='white').place(x=130,y=250)
    
    
    Button(gameWindow,text='Exit',command=Exit,width=20,bg='brown',fg='white').place(x=300,y=250)




def gameEnter():
    
    if 0 < diceNumber.get() <= 3:
        gameStarting()

    else:
        ms.showerror("Error","You can use at most 3 dice or at least 1 dice")    
    
   
    


def Enter():
    global diceNumber
    window = Tk()
    window.title("Dice Rolling Simulator")
    window.geometry("600x400+500+100")

    label0 = Label(window,text = "Dice Rolling Simulator",width=20,font=("bold",20))
    label0.place(x=90,y=53)

    label1 = Label(window,text = "You can use at most 3 dice or at least 1 dice ",width=50,font=("bold",10))
    label1.place(x=50,y=120)

    label2 = Label(window,text = "Dice Number ",width=20,font=("bold",10))
    label2.place(x=80,y=160)

    diceNumber = IntVar()
   
    entry1 = Entry(window,textvar=diceNumber,width=25)
    entry1.place(x=240,y=160)


    Button(text="Enter",command=gameEnter,width=20,bg = "brown",fg="white").place(x=200,y=250)
    

    

Enter()    

mainloop()