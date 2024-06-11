import socket
from tkinter import *
from threading import Thread
import random

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    thread = Thread(target = reciveMsg)
    thread.start()

def askPlayerName():
    global playerName 
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.geometry('800*600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas[nameWindow,width =500,height=500]
    canvas1.pack(fill = "both",expand=True)

    canvas1.create_image(0,0,image = bg,anchor = 'nw')
    canvas1.create_text(screen_width/4.5,screen_height/8,text="Enter Name",font=("Chalkboard SE",60),fill="black")

    nameEntry = Entry(nameWindow,width = 15,justify='center',font=('Chalboard SE',30),bd=5,bg='white')
    nameEntry.place(x=screen_width/7, y=screen_height/5.5)

    button = Button(nameWindow,text="Save",font=("ChalkBoard SE",30),width=11,command=saveName,height=2,bg="#80deea",bd=3)
    button.place(x=screen_width/6,y=screen_height/4)

    nameWindow.resizeable(True,True)
    nameWindow.mainloop()

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def acceptConnection():
    global CLIENTS
    global SERVER

    while True:
        player_socket,addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        print(player_name)
        if(len(CLIENTS.keys())==0):
            CLIENTS[player_name]={'player_type':'player1'}
        else:
            CLIENTS[player_name]={'player_socket'} = player_socket
            CLIENTS[player_name]={"address"}=addr
            CLIENTS[player_name]={"player_name"}=player_name
            CLIENTS[player_name]={"turn"}=False
    
    print(f"Connection established with {player_name}:{addr}")

def createTicket():
    global gameWindow
    global ticketGrid

    mainLable = Label(gameWindow,width=65,height=16,relief='ridge',borderwidth=5,bg='white')
    mainLable.place(x=95,y=119)
    xPos = 105
    yPos = 130
    for row in range(0,3):
        rowList = []
        for col in range(0,9):
            if(platform.system()=='Darwin'):
                boxButton = Button(gameWindow,
                font = ("Chalkborad SE",18),
                borderwidth=3,
                pady=23,
                padx=22,
                bg='#fff176',
                highlightbackground='fff176',
                activebackground='#c5ela5')

                boxButton.place(x=xPos,y=yPos)
            else:
                boxButton = tk.Button(gameWindow,font=("Chalkboard SE",30),width=3,height=2,borderwidth=5,bg="#fff176")
                boxButton.place(x=xPos,y=yPos)
            
            rowList.append(boxButton)
            xPos += 64
        ticketGrid.append(rowList)
        xPos = 105
        yPos +=82

def gameWindow():
    flashNumberLabel = canvas2.create_text(400,screen_height/2.3,
    text="Wainting for others to join....",
    font=("Chalkboard SE",30),fill="#3e2723")

def recivedMsg():
    global SERVER
    global displayedNumberList
    global flashNumberLabel
    global canvas2
    global gameover

    number = [str(i) for i in range(1,91)]
    while True:
        chunk = SERVER.recv(2048).decode()
        if(chunk in number and flashNumberLabel and not gameover):
            flashNumberLabel.append(int(chunk))
            camvas.itemconfigure(flashNumberLabel,text=chunk,font=('Chalkboard SE',60))
        elif('wins the game' in chunk):
            gameover = True
            canvas2.itemconfigure(flashNumberLabel,text=chunk,font=('Chalkboard SE',40))
            