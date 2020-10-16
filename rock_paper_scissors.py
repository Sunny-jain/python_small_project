from tkinter import *
import random

top = Tk()
click=True
top.iconbitmap(r'C:\Users\dell\Documents\Downloads\icon.ico')
top.title("rock, paper, scissors game")
top.resizable(width=False,height=False)

rbutton=""
pbutton=""
sbutton=""
def play():
    global rbutton,pbutton,sbutton
    rbutton=Button(top,text='ROCK',command=lambda:youpick('rock'))
    pbutton=Button(top,text='PAPER',command=lambda:youpick('paper'))
    sbutton=Button(top,text='SCISSORS',command=lambda:youpick('scissors'))
    rbutton.grid(row=0,column=0)
    pbutton.grid(row=0,column=1)
    sbutton.grid(row=0,column=2)
def computer():
    choice=random.choice(['rock','paper','scissors'])
    return choice
def youpick(ypick):
    global click
    cpick=computer()
    if click:
        if ypick == 'rock':
            rbutton.configure(text='ROCK')
            if cpick == 'rock':
                pbutton.configure(text='ROCK')
                sbutton.configure(text='DRAW')
                click = False
            elif cpick == 'paper':
                pbutton.configure(text='PAPER')
                sbutton.configure(text='LOSE')
                click = False
            else:
                pbutton.configure(text='SCISSORS')
                sbutton.configure(text='WIN')
                click = False
        elif ypick=='paper':
            rbutton.configure(text='PAPER')
            if cpick == 'rock':
                pbutton.configure(text='ROCK')
                sbutton.configure(text='WIN')
                click = False
            elif cpick == 'paper':
                pbutton.configure(text='PAPER')
                sbutton.configure(text='DRAW')
                click = False
            else:
                pbutton.configure(text='SCISSORS')
                sbutton.configure(text='LOSE')
                click = False
        else:
            rbutton.configure(text='SCISSORS')
            if cpick == 'rock':
                pbutton.configure(text='ROCK')
                sbutton.configure(text='LOSE')
                click = False
            elif cpick == 'paper':
                pbutton.configure(text='PAPER')
                sbutton.configure(text='WIN')
                click = False
            else:
                pbutton.configure(text='SCISSORS')
                sbutton.configure(text='DRAW')
                click = False
    else:
        rbutton.configure(text='ROCK')
        pbutton.configure(text='PAPER')
        sbutton.configure(text='SCISSORS')
        click = True
play()
top.mainloop()
