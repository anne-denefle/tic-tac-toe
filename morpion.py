from tkinter import * 
import tkinter as tk
from tkinter import messagebox
import tkmacosx as tkm
from tkinter import ttk

window = tk.Tk()
window.title("Tik Tak Toe")
window.resizable(width=False,height=False)

click = True
count = 0

bouton1 = StringVar()
bouton2 = StringVar()
bouton3 = StringVar()
bouton4 = StringVar()
bouton5 = StringVar()
bouton6 = StringVar()
bouton7 = StringVar()
bouton8 = StringVar()
bouton9 = StringVar()

xPhoto = tk.PhotoImage(file="X.png")
oPhoto = tk.PhotoImage(file= "O.png")

def play():
    Button1 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#ffbb99', 
    textvariable=bouton1, command=lambda:press(1, 0, 0))
    Button1.grid(row=0, column=0)

    Button2 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#ffbb99', textvariable=bouton2, command=lambda:press(2, 0, 1))
    Button2.grid(row=0, column=1)

    Button3 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#ffbb99', textvariable=bouton3, command=lambda:press(3, 0, 2))
    Button3.grid(row=0, column=2)

    Button4 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#ff884d', textvariable=bouton4, command=lambda:press(4, 1, 0))
    Button4.grid(row=1, column=0)

    Button5 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#ff884d', textvariable=bouton5, command=lambda:press(5, 1, 1))
    Button5.grid(row=1, column=1)

    Button6 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#ff884d', textvariable=bouton6, command=lambda:press(6, 1, 2))
    Button6.grid(row=1, column=2)

    Button7 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#e64d00', textvariable=bouton7, command=lambda:press(7, 2, 0))
    Button7.grid(row=2, column=0)

    Button8 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#e64d00', textvariable=bouton8, command=lambda:press(8, 2, 1))
    Button8.grid(row=2, column=1)

    Button9 = tkm.Button(window, height=150, width=150, relief='ridge', borderwidth=.5, background='#e64d00', textvariable=bouton9, command=lambda:press(9, 2, 2))
    Button9.grid(row=2, column=2)

def press(num, r, c):
    global count, click

    if click==True :
        labelPhoto=Label(window, image=xPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            bouton1.set('X')
        elif num == 2:
            bouton2.set('X')
        elif num == 3:
            bouton3.set('X')
        elif num == 4:
            bouton4.set('X')
        elif num == 5:
            bouton5.set('X')
        elif num == 6:
            bouton6.set('X')
        elif num == 7:
            bouton7.set('X')
        elif num == 8:
            bouton8.set('X')
        else:
            bouton9.set('X')
        count += 1
        click=False
        checkwin()
    else :
        labelPhoto=Label(window, image=oPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            bouton1.set('O')
        elif num == 2:
            bouton2.set('O')
        elif num == 3:
            bouton3.set('O')
        elif num == 4:
            bouton4.set('O')
        elif num == 5:
            bouton5.set('O')
        elif num == 6:
            bouton6.set('O')
        elif num == 7:
            bouton7.set('O')
        elif num == 8:
            bouton8.set('O')
        else:
            bouton9.set('O')
        count += 1
        click=True
        checkwin()

def checkwin():

    global count, click

    if(bouton1.get() == 'X' and bouton2.get() == 'X' and bouton3.get() == 'X' or
       bouton4.get() == 'X' and bouton5.get() == 'X' and bouton6.get() == 'X' or
       bouton7.get() == 'X' and bouton8.get() == 'X' and bouton9.get() == 'X' or
       bouton1.get() == 'X' and bouton4.get() == 'X' and bouton7.get() == 'X' or
       bouton2.get() == 'X' and bouton5.get() == 'X' and bouton8.get() == 'X' or
       bouton3.get() == 'X' and bouton6.get() == 'X' and bouton9.get() == 'X' or
       bouton1.get() == 'X' and bouton5.get() == 'X' and bouton9.get() == 'X' or
       bouton3.get() == 'X' and bouton5.get() == 'X' and bouton7.get() == 'X'):
        
        messagebox.showinfo("Tic Tac Toe", 'La Souris a gagné !')
        click=True
        count=0
        clear()
        play()
    elif(bouton1.get() == 'O' and bouton2.get() == 'O' and bouton3.get() == 'O' or
       bouton4.get() == 'O' and bouton5.get() == 'O' and bouton6.get() == 'O' or
       bouton7.get() == 'O' and bouton8.get() == 'O' and bouton9.get() == 'O' or
       bouton1.get() == 'O' and bouton4.get() == 'O' and bouton7.get() == 'O' or
       bouton2.get() == 'O' and bouton5.get() == 'O' and bouton8.get() == 'O' or
       bouton3.get() == 'O' and bouton6.get() == 'O' and bouton9.get() == 'O' or
       bouton1.get() == 'O' and bouton5.get() == 'O' and bouton9.get() == 'O' or
       bouton3.get() == 'O' and bouton5.get() == 'O' and bouton7.get() == 'O') :
        
        messagebox.showinfo("Tic Tac Toe", 'Le Chat a gagné !')
        click=True
        count=0
        clear()
        play()
    elif(count == 9):
        messagebox.showinfo("Tic Tac Toe", 'Match nul !')
        click=0
        clear()
        play()

def clear():
    bouton1.set('')
    bouton2.set('')
    bouton3.set('')
    bouton4.set('')
    bouton5.set('')
    bouton6.set('')
    bouton7.set('')
    bouton8.set('')
    bouton9.set('')

    
play()
window.mainloop()

