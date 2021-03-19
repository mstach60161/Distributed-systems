import socket
from threading import Thread

serverIP = "127.0.0.1"
serverPort = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverIP, serverPort))

def sendmessage():
    while True:
        message = input('message: ')
        client.sendall(bytes(message, 'utf-8'))


Thread(target=sendmessage).start()

while True:
    msg = client.recv(1024)
    if not msg:
        break
    print(str(msg, 'utf-8'))
        