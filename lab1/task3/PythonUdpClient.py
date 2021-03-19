import socket

serverIP = "127.0.0.1"
serverPort = 9008
msg_bytes = (300).to_bytes(4, byteorder='little')

number = int.from_bytes(msg_bytes, byteorder='little')

print(number)

print('PYTHON UDP CLIENT')
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(msg_bytes, (serverIP, serverPort))

buff, address = client.recvfrom(1024)
number = int.from_bytes(buff, byteorder='little')
print("received msg: " + str(number))


