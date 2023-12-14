#importing libraries
import tkinter
from playsound import playsound
from threading import Thread

#creating variables
turn = 1
winner = 0
b=["xd lol easter egg","","","","","","","","",""]



#restart function
def restartall():
    global winner
    global turn
    turn = 1
    winner = 0
    global b
    b=["xd lol easter egg","","","","","","","","",""]
    button1.config(text="")
    button2.config(text="")
    button3.config(text="")
    button4.config(text="")
    button5.config(text="")
    button6.config(text="")
    button7.config(text="")
    button8.config(text="")
    button9.config(text="")
    vmessage.config(text="")
    counter.config(text="Player "+ str(turn) + "'s turn")

#Use your own path and sound for victory fanfare
def victorymusic():
    playsound(r"\Path\To\Your\success.mp3")

#victory condition check
def victory():
    global winner
    global turn
    thread = Thread(target=victorymusic)
    if b[1] == b[2] and b[1] == b[3] and b[1] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[4] == b[5] and b[4] == b[6] and b[4] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[7] == b[8] and b[7] == b[9] and b[7] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[1] == b[4] and b[1] == b[7] and b[1] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[2] == b[5] and b[2] == b[8] and b[2] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[3] == b[6] and b[3] == b[9] and b[3] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[1] == b[5] and b[1] == b[9] and b[1] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif b[3] == b[5] and b[3] == b[7] and b[3] !="":
        vmessage.config(text="Player "+ str(winner) + " wins")
        thread.start()
        turn = 0
    elif "" not in b:
        vmessage.config(text="Tie")
        turn = 0
    else:
        counter.config(text="Player "+ str(turn) + "'s turn")


#button text changes and turn change
def b1textchange():
    global turn
    global winner
    if b[1] == "":
        if turn == 1:
            b[1] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[1]= "O"
            winner = 2
            turn = 1
            victory()
        button1.config(text=b[1])


def b2textchange():
    global turn
    global winner
    if b[2] == "":    
        if turn == 1:
            b[2] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[2] = "O"
            winner = 2
            turn = 1
            victory()
        button2.config(text=b[2])

def b3textchange():
    global turn
    global winner
    if b[3] == "":
        if turn == 1:
            b[3] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[3] = "O"
            winner = 2
            turn = 1
            victory()
        button3.config(text=b[3])

def b4textchange():
    global turn
    global winner
    if b[4] == "":
        if turn == 1:
            b[4] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[4] = "O"
            winner = 2
            turn = 1
            victory()
        button4.config(text=b[4])

def b5textchange():
    global turn
    global winner
    if b[5] == "":
        if turn == 1:
            b[5] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[5] = "O"
            winner = 2
            turn = 1
            victory()
        button5.config(text=b[5])

def b6textchange():
    global turn
    global winner
    if b[6] == "":
        if turn == 1:
            b[6] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[6] = "O"
            winner = 2
            turn = 1
            victory()
        button6.config(text=b[6])

def b7textchange():
    global turn
    global winner
    if b[7] == "":
        if turn == 1:
            b[7] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[7] = "O"
            winner = 2
            turn = 1
            victory()
        button7.config(text=b[7])

def b8textchange():
    global turn
    global winner
    if b[8] == "":
        if turn == 1:
            b[8] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[8] = "O"
            winner = 2
            turn = 1
            victory()
        button8.config(text=b[8])

def b9textchange():
    global turn
    global winner
    if b[9] == "":
        if turn == 1:
            b[9] = "x"
            winner = 1
            turn = 2
            victory()
        elif turn == 2:
            b[9] = "O"
            winner = 2
            turn = 1
            victory()
        button9.config(text=b[9])

#creating window
window=tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(width=False, height=False)
window.geometry("150x200")

#creating buttons
button1=tkinter.Button(window, text=b[1],height=2, width=5, command=b1textchange)
button1.place(x=0, y=50)

button2=tkinter.Button(window, text=b[2],height=2, width=5, command=b2textchange)
button2.place(x=50, y=50)

button3=tkinter.Button(window, text=b[3],height=2, width=5, command=b3textchange)
button3.place(x=100, y=50)

button4=tkinter.Button(window, text=b[4],height=2, width=5, command=b4textchange)
button4.place(x=0, y=100)

button5=tkinter.Button(window, text=b[5],height=2, width=5, command=b5textchange)
button5.place(x=50, y=100)

button6=tkinter.Button(window, text=b[6],height=2, width=5, command=b6textchange)
button6.place(x=100, y=100)

button7=tkinter.Button(window, text=b[7],height=2, width=5, command=b7textchange)
button7.place(x=0, y=150)

button8=tkinter.Button(window, text=b[8],height=2, width=5, command=b8textchange)
button8.place(x=50, y=150)

button9=tkinter.Button(window, text=b[9],height=2, width=5, command=b9textchange)
button9.place(x=100, y=150)


#turn counter
counter=tkinter.Label(window, text="Player 1's turn")
counter.place(x=0, y=0)

#victory message
vmessage=tkinter.Label(window, text="")
vmessage.place(x=0, y=20)

#restart
restart=tkinter.Button(window, text="Restart",height=1, width=5, command=restartall)
restart.place(x=100, y=20)

#making window go to the middle of the screen
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()
