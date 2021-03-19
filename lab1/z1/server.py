import socket
from threading import Thread, Lock
from queue import Queue
import time

server_port = 9000

clients = []
lock = Lock()
messages = Queue()

def client_thread(conn, addr):
    print('new client: ' + str(addr))

    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        else:
            print(str(msg, 'utf-8') + ", from: ", addr)
            messages.put((addr, msg),)

def messages_sender():
    while True:
        message = messages.get()
        if message:
            addr, msg = message
            msg = 'msg: ' + str(msg, 'utf-8') + 'from ' + str(addr)
            print(msg)
            lock.acquire()
            for client in clients:
                client.sendall(bytes(msg, 'utf-8'))
            lock.release()
        time.sleep(0.2)


def server_thread():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', server_port))
    server.listen(10)
    print('server started')
    while True:
        conn, addr = server.accept()
        lock.acquire()
        clients.append(conn)
        lock.release()
        Thread(target=client_thread, args=(conn, addr)).start()

Thread(target=server_thread).start()
Thread(target=messages_sender).start()