import socket
from tkinter import *
from tkinter import filedialog
import os
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 50000))
server_socket.listen()

print("Server listening on port 50000...")

conn = None

def waitClient():
    global conn
    conn, addr = server_socket.accept()
    print('Connected by', addr)

threading.Thread(target=waitClient, daemon=True).start()

def selectFile():
    filePath = filedialog.askopenfilename()
    myEntry.delete(0, END)
    myEntry.insert(0, filePath)

def sendFile():
    global conn

    if conn is None:
        print("No client connected")
        return

    filePath = myEntry.get()
    filename = os.path.basename(filePath)

    # إرسال اسم الملف
    # conn.send((filename + "\n").encode())

    with open(filePath, "rb") as f:
        while True:
            data = f.read(1024)   # زي ما كنت كاتب
            if not data:
                break
            conn.sendall(data)

    print("File sent")
    conn.close()

myScreen = Tk()

myEntry = Entry(myScreen, width=40)
myEntry.grid(row=0, column=0, padx=5)

myButton = Button(myScreen, text='Select File', command=selectFile)
myButton.grid(row=0, column=1, padx=5, pady=5)

myButton = Button(myScreen, text='Send File', command=sendFile)
myButton.grid(row=1, column=0, pady=5)

myScreen.mainloop()