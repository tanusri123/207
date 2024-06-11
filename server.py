import socket
from threading import Thread 

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 6000
client = ()

def setup():
    print("\n\t\t\t\t\t*** Welcome To Tambola Game***\n")

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind(IP_ADDRESS,PORT)

    SERVER.listen(10)

    print("\t\t\t\SERVER IS WAITING FOR INCOMING CONNECTION...\n")

def placeNumber():
    global ticketGrid
    global currentNumberList

    for row in range(0,3):
        randomColList = []
        counter = 0
        while counter<=4:
            randomCol = random.randint(0,8)
            if (randomCol not in randomColList):
                randomColList.append(randomCol)
                counter += 1
    numberContainer ={
        "0":[1,2,3,4,5,6,7,8,9],
        "1":[10,11,12,13,14,15,16,17,18,19],
        "2":[20,21,22,23,24,25,26,27,28,29],
        "3":[30,31,32,33,34,35,36,37,38,39],
        "4":[40,41,42,43,44,45,46,47,48,49],
        "5":[50,51,52,53,54,55,56,57,58,59],
        "6":[60,61,62,63,64,65,66,67,68,69],
        "7":[70,71,72,73,74,75,76,77,78,79],
        "8":[80,81,82,83,84,85,86,87,88,89,90],

    }

    counter = 0
    while(counter<len(randomColList)):
        colNum = randomColList[counter]
        numbersListByIndex = numberContainer[str(colNum)]
        randomNumber = random.choice(numbersListByIndex)

        if(randomNumber not in currentNumberList):
            numberBox = ticketGrid[row][colNum]
            numberBox.configure(text=randomNumber,fg="black")
            currentNumberList.append(randomNumber)
            counter += 1